from rest_framework import viewsets, status
from rest_framework.response import Response

from review.service.review_service_impl import ReviewServiceImpl


class ReviewController(viewsets.ViewSet):
    reviewService = ReviewServiceImpl.getInstance()

    def createReviewForm(self, request):
        randomString = request.data.get('randomString')
        reviewId = self.reviewService.createReviewForm(randomString)
        return Response(reviewId, status=status.HTTP_200_OK)

    def registerTitleDescription(self, request):
        reviewId = request.data.get('reviewId')
        reviewTitle = request.data.get('reviewTitle')
        reviewDescription = request.data.get('reviewDescription')
        print(f'reviewId : {reviewId}, reviewTitle: {reviewTitle}, reviewDescription: {reviewDescription}')

        review = self.reviewService.getReviewByReviewId(reviewId)
        result = self.reviewService.registerTitleDescription(review, reviewTitle, reviewDescription)
        return Response(result, status=status.HTTP_200_OK)

    def registerQuestion(self, request):
        reviewId = request.data.get('reviewId')
        questionTitle = request.data.get('questionTitle')
        questionType = request.data.get('questionType')
        essential = request.data.get('isEssential') == 'true'
        images = request.FILES.getlist('images')
        print('reviewId: ', reviewId, 'questionTitle: ', questionTitle, 'questionType: ', questionType,
              'essential: ', essential, 'images: ', images)
        review = self.reviewService.getReviewByReviewId(reviewId)
        result = self.reviewService.registerQuestion(review, questionTitle, questionType, essential, images)
        return Response(result, status=status.HTTP_200_OK)

    def registerSelection(self, request):
        questionId = request.data.get('questionId')
        selection = request.data.get('selection')
        print(f"questionId : {questionId}, selection : {selection}")
        question = self.reviewService.getQuestionByQuestionId(questionId)
        result = self.reviewService.registerSelection(question, selection)
        return Response(result, status=status.HTTP_200_OK)

    def reviewList(self, request):
        reviewTitleList = self.reviewService.getreviewList()
        randomStringList = self.reviewService.getRandomStringList()
        combinedList = []
        for review, random in zip(reviewTitleList, randomStringList):
            combinedItem = {**review, **random}
            combinedList.append(combinedItem)
        return Response({'reviewTitleList': combinedList}, status=status.HTTP_200_OK)

    def readreviewForm(self, request, randomString=None):
        reviewId = self.reviewService.getreviewIdByRandomString(randomString)
        reviewForm = self.reviewService.getServeyById(reviewId)
        print('내보낼 결과 : ', reviewForm)
        return Response(reviewForm, status.HTTP_200_OK)

    def submitReview(self, request):
        try:
            answers = request.data.get('submitForm')
            accountId = request.data.get('accountId')
            print("answers: ", answers, 'accountId :', accountId)

            self.reviewService.saveAnswer(answers, accountId)

            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def pushRandomstring(self, request):
        try:
            reviewId = self.reviewService.getRecentreview()
            data = self.reviewService.getRandomstringByreviewId(reviewId)
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            print('randomString 가져오는 중 문제 발생 : ', e)
            return Response(False, status=status.HTTP_400_BAD_REQUEST)

    def reviewResult(self, request, reviewId=None):
        resultForm = self.reviewService.getResultById(reviewId)
        return Response(resultForm, status.HTTP_200_OK)

    def checkIsFirstSubmit(self, request):
        accountId = request.data.get('accountId')
        isSubmitted = self.reviewService.getAnswerByAccountId(accountId)
        return Response(isSubmitted, status.HTTP_200_OK)
