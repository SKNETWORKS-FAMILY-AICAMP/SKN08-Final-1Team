from django.urls import path, include
from rest_framework.routers import DefaultRouter

from interview.controller.interview_controller import InterviewController

router = DefaultRouter()
router.register(r"interview", InterviewController, basename='interview')

urlpatterns = [
    path('', include(router.urls)),
    path('create',
         InterviewController.as_view({ 'post': 'requestCreateInterview' }),
         name='인터뷰 질문 생성 및 추가'),
    path('list',
         InterviewController.as_view({ 'post': 'requestListInterview' }),
         name='인터뷰 리스트'),
    path('remove',
         InterviewController.as_view({ 'post': 'requestRemoveInterview' }),
         name='인터뷰 제거'),
    path('user-answer',
         InterviewController.as_view({ 'post': 'requestCreateAnswer' }),
         name='인터뷰 사용자 답변 등록'),
]