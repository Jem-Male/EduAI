from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CourseAPIView,
    LessonAPIViews,
    TaskAPIViews,
    QuizAPIViews,
    QuizOptionAPIView,
    SubmissionTaskAPIView,
    AiCourseAPIView
)


router = DefaultRouter()

router.register(r'lessons', LessonAPIViews, basename='lesson')
router.register(r'courses', CourseAPIView, basename='course')
router.register(r'tasks', TaskAPIViews, basename='task')
router.register(r'quizzes', QuizAPIViews, basename='quiz')
router.register(r'quiz-options', QuizOptionAPIView, basename='quiz-option')
router.register(r'submissions', SubmissionTaskAPIView, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
    path('ai/', AiCourseAPIView.as_view()),
]