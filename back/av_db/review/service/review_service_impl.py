from account.repository.account_repository_impl import AccountRepositoryImpl
from review.repository.review_answer_repository_impl import ReviewAnswerRepositoryImpl
from review.repository.review_description_repository_impl import ReviewDescriptionRepositoryImpl
from review.repository.review_question_repository_impl import ReviewQuestionRepositoryImpl
from review.repository.review_repository_impl import ReviewRepositoryImpl
from review.repository.review_selection_repository_impl import ReviewSelectionRepositoryImpl
from review.repository.review_title_repository_impl import ReviewTitleRepositoryImpl
from review.service.review_service import ReviewService


class ReviewServiceImpl(ReviewService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # cls.__instance.__reviewDocumentRepository = reviewDocumentRepositoryImpl.getInstance()
            cls.__instance.__reviewRepository = ReviewRepositoryImpl.getInstance()
            cls.__instance.__reviewTitleRepository = ReviewTitleRepositoryImpl.getInstance()
            cls.__instance.__reviewDescriptionRepository = ReviewDescriptionRepositoryImpl.getInstance()
            cls.__instance.__reviewQuestionRepository = ReviewQuestionRepositoryImpl.getInstance()
            cls.__instance.__reviewSelectionRepository = ReviewSelectionRepositoryImpl.getInstance()
            cls.__instance.__reviewAnswerRepository = ReviewAnswerRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl().getInstance()


        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getRecentreview(self):
        recentId = self.__reviewRepository.getMaxId()
        return recentId

    def createReviewForm(self, randomString):
        maxId = self.__reviewRepository.getMaxId()
        self.__reviewRepository.registerReview(randomString)
        return maxId + 1

    def getReviewByReviewId(self, reviewId):
        review = self.__reviewRepository.findreview(reviewId)
        return review

    def getQuestionByQuestionId(self, questionId):
        question = self.__reviewQuestionRepository.findQuestion(questionId)
        return question

    def registerTitleDescription(self, review, reviewTitle, reviewDescription):
        try:
            titleResult = self.__reviewTitleRepository.registerTitle(review, reviewTitle)
            descriptionResult = self.__reviewDescriptionRepository.registerDescription(review, reviewDescription)
            return titleResult & descriptionResult
        except Exception as e:
            print('설문 제목, 설명 저장 중 오류 발생 : ', e)
            return False

    def registerQuestion(self, review, questionTitle, questionType, essential, images):
        try:
            question = (
                self.__reviewQuestionRepository.registerQuestion(review, questionTitle, questionType, essential, images))
            return question

        except Exception as e:
            print('설문 질문 저장 중 오류 발생 : ', e)
            return False


    def registerSelection(self, question, selection):
        try:
            result = self.__reviewSelectionRepository.registerSelection(question, selection)
            return result
        except Exception as e:
            print('설문 선택 항목 저장 중 오류 발생 : ', e)
            return False

    def getReviewList(self):
        return self.__reviewTitleRepository.getAllTitles()

    def getRandomStringList(self):
        return self.__reviewRepository.getAllRandomString()

    def getServeyById(self, reviewId):
        reviewTitle = self.__reviewTitleRepository.getTitleByreviewId(reviewId)
        reviewDescription = self.__reviewDescriptionRepository.getDescriptionByreviewId(reviewId)
        reviewQuestions = self.__reviewQuestionRepository.getQuestionsByreviewId(reviewId)

        for question in reviewQuestions:
            if question['questionType'] != 'text':
                selection = self.__reviewSelectionRepository.getSelectionsByQuestionId(question['questionId'])
                question['selection'] = selection

        reviewForm = {'reviewId': reviewId, 'reviewTitle': reviewTitle,
                'reviewDescription': reviewDescription, 'reviewQuestions': reviewQuestions}

        return reviewForm

    def saveAnswer(self, answers, account):
        try:
            if account is not None:
                account = self.__accountRepository.findById(account)

            for answer in answers:
                questionId = answer.get('questionId')
                question = self.__reviewQuestionRepository.findQuestion(questionId)

                if answer['questionType'] == 'text':
                    answer = answer.get('answer')
                    textAnswer = self.__reviewAnswerRepository.saveTextAnswer(question, answer, account)

                elif answer['questionType'] == 'radio':
                    selection = answer.get('answer')
                    selection = self.__reviewSelectionRepository.findSelectionBySelectionName(question, selection)
                    checkboxAnswer = self.__reviewAnswerRepository.saveRadioAnswer(question, selection, account)

                elif answer['questionType'] == 'checkbox':
                    selectionNameArray = answer.get('answer')
                    selectionArray = \
                        [self.__reviewSelectionRepository.findSelectionBySelectionName(question, selection) for selection in selectionNameArray]
                    radioAnswer = self.__reviewAnswerRepository.saveCheckboxAnswer(question, selectionArray, account)

        except Exception as e:
            print('답변 저장중 오류 발생: ', {e})

    def getReviewIdByRandomString(self, randomString):
        return self.__reviewRepository.findreviewIdByRandomString(randomString)

    def getRandomstringByreviewId(self,reviewId):
        return self.__reviewRepository.findRandomStringByreviewId(reviewId)

    def getResultById(self, reviewId):
        reviewTitle = self.__reviewTitleRepository.getTitleByreviewId(reviewId)
        reviewDescription = self.__reviewDescriptionRepository.getDescriptionByreviewId(reviewId)
        reviewQuestions = self.__reviewQuestionRepository.getQuestionsByreviewId(reviewId)

        for question in reviewQuestions:
            if question['questionType'] == 'text':
                answer = self.__reviewAnswerRepository.getTextAnswersByQuestionId(question['questionId'])
                question['answer'] = answer
            else:
                selectionAnswer = self.__reviewAnswerRepository.getSelectionAnswersByQuestionId(question['questionId'])
                convertedData = {}
                for selectionId, value in selectionAnswer.items():
                    selectionName = self.__reviewSelectionRepository.findSelectionBySelectionId(selectionId).selection
                    convertedData[selectionName] = value

                question['selection'] = convertedData
        resultForm = {'reviewId': reviewId, 'reviewTitle': reviewTitle,
                'reviewDescription': reviewDescription, 'reviewQuestions': reviewQuestions}
        print('resultForm 생성이 완료되었습니다 : \n', resultForm)
        return resultForm

    def getAnswerByAccountId(self, accountId):
        accountId = self.__accountRepository.findById(accountId)
        isSubmitted = self.__reviewAnswerRepository.getAnswerByAccountId(accountId)
        return isSubmitted







