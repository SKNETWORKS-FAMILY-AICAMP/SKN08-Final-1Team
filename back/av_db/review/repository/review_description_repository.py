from abc import ABC, abstractmethod


class ReviewDescriptionRepository(ABC):
    @abstractmethod
    def registerDescription(self, review, reviewDescription):
        pass

    @abstractmethod
    def getDescriptionByReviewId(self, reviewId):
        pass

