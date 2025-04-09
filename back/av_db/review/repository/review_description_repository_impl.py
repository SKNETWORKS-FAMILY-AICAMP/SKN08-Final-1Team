from review.entity.review_description import ReviewDescription
from review.repository.review_description_repository import ReviewDescriptionRepository


class ReviewDescriptionRepositoryImpl(ReviewDescriptionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def registerDescription(self, review, reviewDescription):
        try:
            ReviewDescription.objects.create(review_id=review, description=reviewDescription)
            return True

        except Exception as e:
            print('Description 저장 중 오류 발생 : ', e)
            return False

    def getDescriptionByReviewId(self, reviewId):
        description = ReviewDescription.objects.get(review_id=reviewId)
        return description.description






