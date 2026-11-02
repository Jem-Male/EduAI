from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseAPIView, LessonAPIViews


router = DefaultRouter()

router.register(r'lessons', LessonAPIViews, basename='lesson')
router.register(r'courses', CourseAPIView, basename='course')


urlpatterns = [
    path('', include(router.urls)),
]