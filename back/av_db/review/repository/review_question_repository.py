from abc import ABC, abstractmethod

class ReviewQuestionRepository(ABC):
    @abstractmethod
    def registerQuestion(self, review, questionTitle, questionType, essential, images):
        pass

    @abstractmethod
    def findQuestion(self, questionId):
        pass

    @abstractmethod
    def getQuestionsByReviewId(self, reviewId):
        pass