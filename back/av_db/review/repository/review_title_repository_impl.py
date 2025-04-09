from review.entity.review_title import ReviewTitle
from review.repository.review_title_repository import ReviewTitleRepository

class ReviewTitleRepositoryImpl(ReviewTitleRepository):
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

    def registerTitle(self, review, reviewTitle):
        try:
            ReviewTitle.objects.create(review_id=review, title=reviewTitle)
            return True

        except Exception as e:
            print('Title 저장 중 오류 발생 : ', e)
            return False

    def getAllTitles(self):
        reviewTitleAll = ReviewTitle.objects.all().order_by('review_id')
        reviewTitleList = [{'reviewId': review.review_id.id, 'reviewTitle': review.title} for review in reviewTitleAll]
        return reviewTitleList

    def getTitleByReviewId(self, reviewId):
        reviewTitle = ReviewTitle.objects.get(review_id=reviewId)

        return reviewTitle.title





