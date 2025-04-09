import json
import os
from datetime import datetime, timedelta

from dart_fss.api.filings import get_corp_code
from dart_fss.api.filings import get_corp_info
from dotenv import load_dotenv

import dart_fss as dart
import openai
from bs4 import BeautifulSoup

from making_report.repository.data_for_corp_business_repository import DataForCorpBusinessRepository


load_dotenv()

dartApiKey = os.getenv('DART_API_KEY')
if dartApiKey is None:
    raise ValueError("Dart API Key가 준비되어 있지 않습니다.")

openaiApiKey = os.getenv('OPEN_API_KEY')
if openaiApiKey is None:
    raise ValueError("API Key가 준비되어 있지 않습니다.")


class DataForCorpBusinessRepositoryImpl(DataForCorpBusinessRepository):
    __instance = None

    # 원하는 공시 정보 기업 리스트
    WANTED_CORP_LIST = [
        "SK네트웍스", "삼성전자", "현대자동차", "SK하이닉스", "LG전자", "POSCO홀딩스", "NAVER", "현대모비스", "기아", "LG화학", "삼성물산", "롯데케미칼",
        "SK이노베이션", "S-Oil", "CJ제일제당", "현대건설", "삼성에스디에스", "LG디스플레이", "아모레퍼시픽", "한화솔루션", "HD현대중공업", "LS", "SK텔레콤", "케이티",
        "LG유플러스", "HJ중공업", "삼성전기", "한화에어로스페이스", "효성", "코웨이", "한샘", "신세계", "이마트", "현대백화점", "LG생활건강", "GS리테일", "오뚜기",
        "농심", "롯데웰푸드", "CJ ENM", "한화", "LG이노텍", "삼성바이오로직스", "셀트리온"
    ]
    # 1년 사이의 공시 정보를 가져옵니다 => 2024년 1월 1일 ~
    SEARCH_YEAR_GAP = 1
    WANTED_SEARCH_YEAR = f'{(datetime.today() - timedelta(days=365 * SEARCH_YEAR_GAP)).year}0101'
    WANTED_SEARCH_DOC = 'A' # A: 정기공시, B: 주요사항보고, C: 발행공시, D: 지분공시, E: 기타공시, F: 외부감사관련, G: 펀드공시, H: 자산유동화, I: 거래소공시, J: 공정위공시

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            dart.set_api_key(api_key=dartApiKey)
            openai.api_key = openaiApiKey
            cls.__instance.__totalCorpList = dart.get_corp_list()
            cls.__instance.__wantedCorpCodeDict = cls.__instance.getCorpCode()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # {"회사 명": "고유 번호"}를 가져옵니다.
    def getCorpCodeDict(self):
        return self.__wantedCorpCodeDict

    # 잘못된 기업 명을 입력할 경우 오류가 발생합니다.
    def alarmWrongRegisteredCorpName(self, name, corp):
        if not corp:
            print(f'기업명 입력 오류 "{name}"')
            expectedCorp = self.__totalCorpList.find_by_corp_name(name, exactly=False, market='YKN')

            if expectedCorp:
                print(f'-> 예상 변경 이름 {[corp.corp_name for corp in expectedCorp]}')

        return name

    # 고유 번호가 2개 이상인 기업인 경우
    def alarmMultiRegisteredCorpNames(self, name, corp):
        if isinstance(corp, list) and len(corp) >= 2:
            raise ValueError(f'기업명 "{name}" {len(corp)} 개 검색이 됩니다.')

    def getCorpCode(self):
        corpCodeDict = {}
        wrongInput = []

        # 원하는 공시 정보 기업 리스트에서 기업 명 별 공시 정보를 가져옵니다.
        for name in self.WANTED_CORP_LIST:
            corp = self.__totalCorpList.find_by_corp_name(name, exactly=True, market="YKN")
            if corp is None:
                wrongInput.append(
                    self.alarmWrongRegisteredCorpName(name, corp)
                )
            else:
                if wrongInput:
                    continue
                corpCodeDict[name] = corp[0].corp_code

            self.alarmMultiRegisteredCorpNames(name, corp)

        if wrongInput:
            raise ValueError(f"기업명 입력이 잘못되었습니다. {wrongInput}")

        return corpCodeDict

    # Dart에서 사업보고서를 가져와 /assets/company_data에 저장합니다.
    def getRawBusinessDataFromDart(self):
        rawSummaryDict, rawTableDict = {}, {}
        for corpName in self.WANTED_CORP_LIST:
            filePath = "../assets/company_data/"
            # html 형식으로 저장된 파일을 읽기 모드로 엽니다.
            with open(f"{filePath}{corpName}.html", "r", encoding="utf-8-sig") as f:
                companyHtml = f.read()

            # 저장된 파일을 html.parser 구문기로 엽니다.
            companySoup = BeautifulSoup(companyHtml, "html.parser")

            companyData = []

            # 파일에서 "h1" 태그에 해당되는 요소들을 모두 가져옵니다.
            for tag in companySoup.find_all("h1"):
                companyData.append(tag.find_text())
            rawSummaryDict[corpName] = str(companyData[0])
            rawTableDict[corpName] = {"revenueTable": str(companyData[1])}

        return rawSummaryDict, rawTableDict

    # gpt-4o-mini를 활용해 promprtengineering(컨텐츠 형식 바꿈) 합니다.
    # def changeContentStyle(self, businessData):
    #     maxTokenLength = 128000
    #     promptEngineering = f"""
    #     사용자 입력 메시지의 내용은 한국기업의 사업내용이다. 너는 기업을 전문적으로 분석하는 유능한 분석가이다.
    #     모든 <조건>에 맞춰, <구조>과 같은 구조로 한국기업의 사업내용을 요약하라.
    #
    #     <조건>
    #     1. 개조식으로 작성할 것.
    #         (예시: [BEFORE] 회사는 지속적인 기술 및 서비스에 대한 투자를 통해 핵심 사업의 경쟁력을 강화하고 있습니다. -> [AFTER] 지속적인 기술 및 서비스에 대한 투자를 통해 핵심 사업의 경쟁력을 강화)
    #     2. 1500 token 내로 작성을 마무리할 것.
    #     3. 첫 문단은 취업준비생들을 위해 요청한 사업내용 요약에 대한 전반적인 총평과 기업 공략 포인트에 대해서 정리해서 기재할 것.
    #     4. 첫 문단 이후에 요청한 사업내용 요약을 기재할 것.
    #
    #     <구조>
    #     1. 글을 HTML 형식으로 요약할 것
    #     2. 목록은 <ul>과 <li> 태그로 표현할 것.
    #     3. 태그 사이에 띄어쓰기('\n') 없이 한 줄로 표현할 것.
    #     예시:
    #     <p>첫 문단(전반적인 총평과 기업 공략 포인트)</p><ul><li>상위 목록 항목 1<ul><li>하위 목록 항목 1.1</li><li>하위 목록 항목 1.2</li></ul></li><li>상위 목록 항목 2<ul><li>하위 목록 항목 2.1</li><li>하위 목록 항목 2.2</li></ul></li></ul>
    #     """
    #
    #     with openai.OpenAI() as client:
    #         changedContextDict = {}
    #         for corpName, doc in businessData.items():
    #             print(f"* CB_AI - {corpName}")
    #             if len(doc) >= maxTokenLength:
    #                 print(f"사업내용 토큰 수 초과 -> {corpName}")
    #                 continue
    #
    #             messages = [
    #                 {"role": "system", "content": promptEngineering},
    #                 {"role": "user", "content": doc}
    #             ]
    #
    #             response = client.chat.completions.create(
    #                 model="gpt-4o-mini",
    #                 messages=messages,
    #                 max_tokens=1500,    # <= 16,384
    #                 temperature=0.8,
    #             )
    #
    #             changedContextDict[corpName] = {
    #                 "businessSummary": response.choices[0].message.content
    #             }
    #
    #     return changedContextDict
