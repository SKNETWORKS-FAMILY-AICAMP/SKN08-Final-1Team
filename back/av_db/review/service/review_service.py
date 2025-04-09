from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def createReviewForm(self, randomString):
        pass

    @abstractmethod
    def getReviewByReviewId(self, reviewId):
        pass

    @abstractmethod
    def getQuestionByQuestionId(self, questionId):
        pass

    @abstractmethod
    def registerTitleDescription(self, review, reviewTitle, reviewDescription):
        pass

    @abstractmethod
    def registerQuestion(self, review, questionTitle, questionType, essential, images):
        pass

    @abstractmethod
    def registerSelection(self, question, selection):
        pass

    @abstractmethod
    def getReviewList(self):
        pass

    @abstractmethod
    def getRandomStringList(self):
        pass

    @abstractmethod
    def getServeyById(self, reviewId):
        pass

    @abstractmethod
    def saveAnswer(self, answers, accountId):
        pass

    @abstractmethod
    def getReviewIdByRandomString(self, randomString):
        pass

    @abstractmethod
    def getResultById(self, reviewId):
        pass

    @abstractmethod
    def getAnswerByAccountId(self, accountId):
        pass
