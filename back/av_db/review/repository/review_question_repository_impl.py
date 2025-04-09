import os

from review.entity.review_image import ReviewImage
from review.entity.review_question import ReviewQuestion
from review.repository.review_question_repository import ReviewQuestionRepository

class ReviewQuestionRepositoryImpl(ReviewQuestionRepository):
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

    def registerQuestion(self, review, questionTitle, questionType, essential, images):
        try:
            ReviewQuestion.objects.create(review_id=review, question=questionTitle,
                                          question_type=questionType, essential=essential)
            questionId = ReviewQuestion.objects.get(review_id=review, question=questionTitle, question_type=questionType, essential=essential)
            # if len(images) !=0:
            #     for image in images:
            #         ReviewImage.objects.create(question_id=questionId, image=image.name)
            #         uploadDirectory = '..\\..\\aview-nuxt-frontend\\src\\assets\\images\\uploadimages'
            #         imagePath = os.path.join(uploadDirectory, image.name)
            #         with open(imagePath, 'wb+') as destination:
            #             for chunk in image.chunks():
            #                 destination.write(chunk)
            #         print('이미지 경로: ', imagePath)

            return questionId.id

        except Exception as e:
            print('Question 저장 중 오류 발생 : ', e)
            return False

    def findQuestion(self, questionId):
        question = ReviewQuestion.objects.get(id=questionId)
        return question

    def getQuestionsByReviewId(self, reviewId):
        questions = ReviewQuestion.objects.filter(review_id=reviewId)
        questionList = questions.order_by('id').values_list('id', 'question', 'question_type', 'essential')
        images = []
        for question in questions:
            questionImage = ReviewImage.objects.filter(question_id=question).order_by('id').values_list('question_id', 'image')
            images.append(questionImage)

        questionImageList = [item for queryset in images for item in queryset]
        print('questionImageList: ', questionImageList)

        questionList = list(questionList)
        for i, q in enumerate(questionList) :
            if q[2] == 'checkbox':
                questionList[i] = {'questionId': q[0], 'questionTitle': q[1], 'questionType': q[2], 'essential': q[3],
                                   'answer': [], 'images': [image for qId, image in questionImageList if qId == q[0]]}
            else :
                questionList[i] = {'questionId': q[0], 'questionTitle': q[1], 'questionType': q[2], 'essential': q[3],
                                   'answer': '', 'images': [image for qId, image in questionImageList if qId == q[0]]}
        return questionList



