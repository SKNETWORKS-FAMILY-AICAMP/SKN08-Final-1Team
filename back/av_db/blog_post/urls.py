from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog_post.controller.blog_post_controller import BlogPostController

router = DefaultRouter()
router.register(r"blog-post", BlogPostController, basename='blog-post')

urlpatterns = [
    path('', include(router.urls)),
    path('list',
         BlogPostController.as_view({ 'get': 'requestBlogPostList' }),
         name='블로그 포스트 항목 요청'),
    path('upload',
         BlogPostController.as_view({ 'post': 'requestUploadBlogPost' }),
         name='블로그 포스트 s3 업로드'),
    path('create',
         BlogPostController.as_view({ 'post': 'requestCreateBlogPost' }),
         name='블로그 포스트 등록 요청'),
    path('read/<int:pk>',
         BlogPostController.as_view({ 'get': 'requestReadBlogPost' }),
         name='블로그 포스트 읽기 요청'),
    path('update/<int:pk>',
         BlogPostController.as_view({ 'put': 'requestUpdateBlogPost' }),
         name='블로그 포스트 수정 요청'),
    path('delete/<int:pk>',
         BlogPostController.as_view({'delete': 'requestDeleteBlogPost' }),
         name='블로그 포스트 삭제 요청'),
]