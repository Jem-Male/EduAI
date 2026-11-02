from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_hello, post, query, patch, safe_query, CourseAPIView, LessonAPIViews


router = DefaultRouter()

router.register(r'lessons', LessonAPIViews, basename='lesson')

urlpatterns = [
    path('hel/', get_hello, name='hello'), 
    path('post/', post, name='post'),
    path('q/', query, name='query'),
    path('patch/<str:name>/', patch, name='patch'),
    path('sq/', safe_query, name='safe_query'),
    path('courses/<int:pk>/', CourseAPIView.as_view()),
    path('courses/', CourseAPIView.as_view()),
    path('', include(router.urls)),
]