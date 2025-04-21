from abc import ABC, abstractmethod


class InterviewAnswerRepository(ABC):

    @abstractmethod
    def save(self, interviewAnswer: InterviewAnswer) -> InterviewAnswer | None:
        pass