from review.entity.review import Review
from review.repository.review_repository import ReviewRepository


class ReviewRepositoryImpl(ReviewRepository):
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

    def getMaxId(self):
        review = Review.objects.all()
        reviewMaxId = len(review)
        return reviewMaxId

    def registerReview(self, randomString):
        Review.objects.create(review=randomString)

    def findReview(self, reviewId):
        review = Review.objects.get(id=reviewId)
        return review

    def getAllRandomString(self):
        allReview = Review.objects.all()
        randomStringList = [{'randomString': review.review } for review in allReview]
        return randomStringList

    def findReviewIdByRandomString(self, randomString):
        review = Review.objects.get(review=randomString)
        return review.id
    def findRandomStringByReviewId(self, reviewId):
        review = Review.objects.get(id=reviewId)
        return review.review




