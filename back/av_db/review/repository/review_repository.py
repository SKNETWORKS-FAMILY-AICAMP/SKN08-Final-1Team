from abc import ABC, abstractmethod


class ReviewRepository(ABC):
    @abstractmethod
    def getMaxId(self):
        pass

    @abstractmethod
    def registerReview(self, reviewId):
        pass

    @abstractmethod
    def findReview(self, reviewId):
        pass

    @abstractmethod
    def getAllRandomString(self):
        pass

    @abstractmethod
    def findReviewIdByRandomString(self, randomString):
        pass

    @abstractmethod
    def findRandomStringByReviewId(self, reviewId):
        pass