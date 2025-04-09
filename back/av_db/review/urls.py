from django.urls import path, include
from rest_framework.routers import DefaultRouter

from review.controller.review_controller import ReviewController

router = DefaultRouter()
router.register(r'review', ReviewController, basename='review')

urlpatterns = [
    path('creat-form', ReviewController.as_view({'post': 'createReviewForm'}), name='review생성'),
    path('register-title-description', ReviewController.as_view({'post': 'registerTitleDescription'}), name='register-title-description'),
    path('register-question', ReviewController.as_view({'post': 'registerQuestion'}), name='review-question'),
    path('register-selection', ReviewController.as_view({'post': 'registerSelection'}), name='review-selection'),
    path('review-title-list', ReviewController.as_view({'get': 'reviewList'}), name='review-title-list'),
    path('read-review-form/<str:randomString>', ReviewController.as_view({'get': 'readSurveyForm'}), name='read-review-form'),
    path('submit-review', ReviewController.as_view({'post': 'submitSurvey'}), name='submit-review'),
    path('randomstring',ReviewController.as_view({'post':'pushRandomstring'}),name='push-randomstring'),
    path('review-result/<int:surveyId>', ReviewController.as_view({'get': 'surveyResult'}), name='review-result'),
    path('check-first-submit', ReviewController.as_view({'post': 'checkIsFirstSubmit'}), name='check-first-submit'),
]