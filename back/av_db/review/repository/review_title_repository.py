from abc import ABC, abstractmethod


class ReviewTitleRepository(ABC):
    @abstractmethod
    def registerTitle(self, review, reviewTitle):
        pass

    @abstractmethod
    def getAllTitles(self):
        pass

    @abstractmethod
    def getTitleByReviewId(self, reviewId):
        pass

