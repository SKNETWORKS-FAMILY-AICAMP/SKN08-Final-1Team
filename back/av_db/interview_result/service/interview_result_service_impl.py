from account.repository.account_repository_impl import AccountRepositoryImpl
from interview_result.repository.interview_result_repository_impl import InterviewResultRepositoryImpl
from interview_result.service.interview_result_service import InterviewResultService
from interview.entity.interview_question import InterviewQuestion
from interview.entity.interview_answer import InterviewAnswer
from utility.http_client import HttpClient

import json
class InterviewResultServiceImpl(InterviewResultService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__interviewResultRepository = InterviewResultRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def saveInterviewResult(self, accountId):
        return  self.__interviewResultRepository.saveInterviewResult(accountId)

    def getInterviewResult(self, accountId):
        account = self.__accountRepository.findById(accountId)
        print(f"▶ account: {account}")
        interviewResult = self.__interviewResultRepository.getLastInterviewResult(account)
        print(f"▶ interviewResult: {interviewResult}")

        if not interviewResult:
            print("❗️해당 계정의 인터뷰 결과가 없습니다.")
            return []
        interviewResultList = self.__interviewResultRepository.getLastInterviewResultQASList(interviewResult)
        print(f"▶ interviewResultList(raw): {interviewResultList}")
        return interviewResultList

    def getFullQAList(self, interviewId: int) -> tuple[list[str], list[str]]:
        print("들어옴")
        questions = list(
            InterviewQuestion.objects.filter(interview_id=interviewId)
            .order_by("id")
            .values_list("content", flat=True)
        )
        answers = list(
            InterviewAnswer.objects.filter(interview_id=interviewId)
            .order_by("question_id")
            .values_list("answer_text", flat=True)
        )
        print("나감")
        return questions, answers

    def saveQAScoreList(self, interview_result, qa_scores):
        return self.__interviewResultRepository.saveQAScoreList(interview_result, qa_scores)

