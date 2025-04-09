import json
import os
import dart_fss as dart
from datetime import datetime, timedelta
import warnings

import pandas as pd
import requests
from bs4 import BeautifulSoup
from jsonschema.benchmarks.useless_applicator_schemas import baseline

from making_report.repository.data_for_corp_business_repository_impl import dartApiKey

warnings.filterwarnings('ignore')

from dotenv import load_dotenv

from making_report.repository.data_for_finance_repository import DataForFinanceRepository

load_dotenv()

dartApiKey = os.getenv('DART_API_KEY')
if dartApiKey is None:
    raise ValueError("Dart API Key가 준비되어 있지 않습니다.")


# 주요 경영 사항 신고를 가져옵니다.
class DataForFinanceRepositoryImpl(DataForFinanceRepository):
    __instance = None

    SEARCH_YEAR_GAP = 1
    SEARCH_START_YEAR = f'{(datetime.today() - timedelta(days=365 * SEARCH_YEAR_GAP)).year}'
    SEARCH_END_YEAR = f'{datetime.today().year}1231'

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            dart.set_api_key(dartApiKey)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 단일 회사 전체 재무제표를 가져옵니다.
    def parsingFromOpenAPI(self, corpCode):
        url = "https://opendart.fss.or/kr/api/fnlttSinglAcntAll.xml"
        params = {
            'crtfc_key': dartApiKey,    # API 인증키
            'corp_code': corpCode,      # 고유 번호
            'bsns_year': 2024,          # 사업 연도
            'reprt_code': '11011',  # 보고서 코드
            'fs_div': "OFS" # 개별/연결구분 (OFS: 재무제표, CFS: 연괄재무제표)
        }
        response = requests.get(url, params=params)
        return BeautifulSoup(response.content, 'lxml-xml')

    # tag_dict에 해당하는 데이터를 찾아 데이터 프레임을 만듭니다.
    def getFinancialStatements(self, parsedData, financialStatementsType):
        tag_dict = {
            'account_nm': '계정명',
            'account_detail': '계정상세',
            'thstrm_nm': '당기명',
            'thstrm_amount': '당기금액',
            'thstrm_add_amount': '당기누적금액',
            'frmtrm_nm': '전기명',
            'frmtrm_amount': '전기금액',
            'frmtrm_q_nm': '전기명(분/반기)',
            'frmtrm_q_amount': '전기금액(분/반기)',
            'frmtrm_add_amount': '전기누적금액',
            'bfefrmtrm_nm': '전전기명',
            'bfefrmtrm_amount': '전전기금액',
            'ord': '계정과목 정렬순서',
            'currency': '통화 단위',
            'bsns_year': '사업 연도'
        }

        try:
            values = []
            for lst in parsedData.findAll('list'):
                if lst.find('sj_nm').text == financialStatementsType:
                    v = []
                    for tag in tag_dict:
                        try:
                            value = lst.find(tag).text
                        except:
                            value = ''
                        v.append(value)
                    values.append(v)

            temp = pd.DataFrame(values, columns=tag_dict.values())
            df = temp[['계정명', '당기금액', '전기금액', '전전기금액']]

            businessYear = int(temp['사업 연도'].unique()[0])

            df = df.rename(
                columns={
                    '당기금액': (businessYear),
                    '전기금액': (businessYear - 1),
                    '전전기금액': (businessYear - 2),
                }
            )
            df = df.set_index('계정명')

            return df

    # 포괄손익 계산서를 추출합니다.
    def selectIncomeDocument(self, parsedData):
        incomeDf = self.getFinancialStatements(parsedData, "손익계산서")
        comprehensiveIncomeDf = self.getFinancialStatements(parsedData, "포괄손익계산서")

        if comprehensiveIncomeDf is None:
            return incomeDf

        if incomeDf is None:
            return comprehensiveIncomeDf

        return incomeDf

    #
    def checkLabelNameInFS(self, dfIndex, *probableNames):
        for index in dfIndex:
            if any(keyword in "".join(index) for keyword in probableNames):
                return index
            else:
                continue

        return 0

    def checkExactLabelNameInFS(self, dfIndex, *probableNames):
        for index in dfIndex:
            if any(keyword == index for keyword in probableNames):
                return index
            else:
                continue

        return 0

    # 수익 현황을 가져옵니다.
    def getRevenueTrend(self, income):
        name = self.checkLabelNameInFS(
            income.index,
            "매출액",
            "영업수익",
            "수익(매출액)",
        )
        if name == 0:
            name = "매출"

        return income.loc[name].squeeze().to_dict()

    # 영업 이익을 가져옵니다.
    def getProfitTrend(self, income):
        name = self.checkLabelNameInFS(
            income.index, "영업이익"
        )
        return income.loc[name].squeeze().to_dict()

    # 자산 총계에서 부채 총계를 제외한 결과를 가져옵니다.
    def getOwnersCapital(self, balance):
        totalAssetsName = self.checkLabelNameInFS(
            balance.index, "자산총계", "자산 총계"
        )
        totalLibilityName = self.checkExactLabelNameInFS(
            balance.index, "부채총계", "부채 총계"
        )

        totalAssets = balance.loc[totalAssetsName].astype(int).squeeze()
        totalLibility = balance.loc[totalLibilityName].astype(int).squeeze()

        return (totalAssets - totalLibility).to_dict()

    #
    def getFinancialDataFromDart(self, corpCodeDict):
        financialDataDict = {}

        for corpName, corpCode in corpCodeDict.items():
            print(f"* FS Extract - {corpName}")
            parsedData = self.parsingFromOpenAPI(corpCode)

            try:
                balance = self.getFinancialStatements(parsedData, "재무상태표")
                income = self.selectIncomeDocument(parsedData)

                if all([(balance is None), (income is None)]):
                    print(f"[FS_Docu Not Exists] - '{corpName} ({corpCode}")

                revenueTrend = self.getRevenueTrend(income)
                profitTrend = self.getProfitTrend(income)
                ownersCapital = self.getOwnersCapital(baseline)

            except Exception as e:
                print(f"[NOT_PASS '{corpName}({corpCode})-FSValue'] => {e}")
                revenueTrend, profitTrend, ownersCapital = 0, 0, 0
                pass

            financialDataDict[corpName] = {
                "revenueTrend": revenueTrend,
                "profitTrend": profitTrend,
                "ownersCapital": ownersCapital
            }

        return financialDataDict

