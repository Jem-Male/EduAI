# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from .models import Course, Lesson, Task, Quiz, QuizOption, SubmissionTask, SubmissionQuiz
from .serializers import (
    CourseSerializer,
    LessonSerializer,
    QuizSerializer,
    TaskSerializer,
    QuizOptionSerializer,
    SubmissionTaskSerializer,
    SubmissionQuizSerializer
)
from .permissions import IsAdminOrTeacherOrReadOnly, IsSlover


class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]


class LessonAPIViews(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]


class TaskAPIViews(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]


class QuizAPIViews(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    permission_classes = [IsAdminOrTeacherOrReadOnly]


class SubmissionTaskViewSet(ModelViewSet):
    serializer_class = SubmissionTaskSerializer
    permission_classes = [IsSlover]
    
    def get_queryset(self): # type: ignore
        return SubmissionTask.objects.filter(
            user=self.request.user
        )
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)