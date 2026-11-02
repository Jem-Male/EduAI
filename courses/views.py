# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsAdminOrTeacherOrReadOnly


class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]


class LessonAPIViews(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]