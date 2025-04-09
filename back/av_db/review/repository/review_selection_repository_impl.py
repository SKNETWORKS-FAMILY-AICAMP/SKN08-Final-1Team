from review.entity.review_selection import ReviewSelection
from review.repository.review_selection_repository import ReviewSelectionRepository


class ReviewSelectionRepositoryImpl(ReviewSelectionRepository):
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

    def registerSelection(self, question, selection):
        try:
            ReviewSelection.objects.create(review_question_id=question, selection=selection)
            serveySelection = ReviewSelection.objects.get(review_question_id=question, selection=selection)

            return serveySelection.id

        except Exception as e:
            print('Selection 저장 중 오류 발생 : ', e)

    def getSelectionsByQuestionId(self, questionId):
        selections = ReviewSelection.objects.filter(review_question_id=questionId).order_by('id').values_list('selection')
        listSelections = []
        for s in selections :
            listSelections.append(s[0])

        return listSelections

    def findSelectionBySelectionId(self, selectionId):
        selection = ReviewSelection.objects.get(id=selectionId)
        return selection

    def findSelectionBySelectionName(self, question, selectionName):
        selection = ReviewSelection.objects.get(review_question_id=question, selection=selectionName)
        return selection





