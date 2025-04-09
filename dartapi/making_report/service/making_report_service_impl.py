import json
import os

from making_report.repository.data_for_corp_business_repository_impl import DataForCorpBusinessRepositoryImpl
from making_report.repository.data_for_corp_overview_repository_impl import DataForCorpOverviewRepositoryImpl
from making_report.repository.data_for_finance_repository_impl import DataForFinanceRepositoryImpl
from making_report.repository.making_report_repository_impl import MakingReportRepositoryImpl
from making_report.service.making_report_service import MakingReportService


class MakingReportServiceImpl(MakingReportService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__corpBusinessRepository = DataForCorpBusinessRepositoryImpl.getInstance()
            cls.__instance.__corpOverviewRepository = DataForCorpOverviewRepositoryImpl.getInstance()
            cls.__instance.__financeRepository = DataForFinanceRepositoryImpl.getInstance()
            cls.__instance.__reportRepository = MakingReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def makingReport(self, request):
        fileList = os.listdir("./assets")

        if "report.json" not in fileList:
            corpCodeDict = self.__corpBusinessRepository.getCorpCodeDict()

            print(f"* CORP_OVERVIEW start ----------------")
            corpOverviewRawData = self.__corpOverviewRepository.getRawOverviewDataFromDart(corpCodeDict)
            corpOverviewPreprocessdData = self.__corpOverviewRepository.preprocessRawData(corpOverviewRawData)

            print(f"* CORP_BUSINESS start ---------------")
            rawSummaryDict, rawTableDict = self.__corpBusinessRepository.getRawBusinessDataFromDart()
            corpBusinessSummary = self.__corpBusinessRepository.changeContentStyle(rawSummaryDict)

            print(f"* FINANCIAL_STATEMENTS start --------------")
            financeProfitDict = self.__financeRepository.getFinancialDataFromDart(corpCodeDict)

            print(f"* REPORT start -------------")
            makeReport = self.__reportRepository.gatherDate(
                corpCodeDict.keys(),
                corpOverviewPreprocessdData,
                financeProfitDict,
                corpBusinessSummary,
                rawTableDict
            )
        else:
            with open("./assets/report.json", "r", encoding="utf-8-sig") as f:
                makeReport = json.load(f)

        return {"aiResult": makeReport}