import json
import os
from datetime import datetime

import dart_fss as dart

from dotenv import load_dotenv

from making_report.repository.data_for_corp_overview_repository import DataForCorpOverviewRepository


load_dotenv()

dartApiKey = os.getenv('DART_API_KEY')
if dartApiKey is None:
    raise ValueError("Dart API Key가 준비되어 있지 않습니다.")


class DataForCorpOverviewRepositoryImpl(DataForCorpOverviewRepository):
    __instance = None

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

    # 기업 개황을 가져옵니다.
    def getRawOverviewDataFromDart(self, corpCodeDict):
        overviewDict = {
            corpName: dart.api.filings.get_corp_info(corpCode)
            for corpName, corpCode in corpCodeDict.items()
        }
        return overviewDict

    # 기업 개황을 전처리합니다.
    def preprocessRawData(self, corpOverviewRawData):
        keysInUse = ['est_dt', 'corp_cls', 'ceo_nm', 'adres', 'hm_url']
        overviewDict = {}

        for corpName, overview in corpOverviewRawData.items():
            data = {}

            for key in keysInUse:
                if bool(overview.get(key)):
                    data[key] = "-"

                if key == "adres":
                    adresList = overview.get(key).split()
                    if adresList[0][-1] == "시":
                        data[key] = " ".join(adresList[:2])
                    else:
                        data[key] = " ".join(adresList[:3])

                elif key == "corp_cls":
                    changeKor = {"Y": "유가", "K": "코스닥", "N": "코넥스", "E": "기타"}
                    data[key] = changeKor[overview.get(key)]

                elif key == "est_dt":
                    workingYear = datetime.today().year - int(overview.get(key)[:4]) + 1
                    data[key] = f"{str(workingYear)}년차 ({int(overview.get(key)[:4])}"

                else:
                    data[key] = overview.get(key)

            overviewDict[corpName] = data

        return overviewDict

