from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Course, Lesson, Task, Quiz, QuizOption, SubmissionTask, SubmissionQuiz
from .serializers import (
    CourseSerializer,
    LessonSerializer,
    QuizSerializer,
    TaskSerializer,
    QuizOptionSerializer,
    SubmissionTaskSerializer,
    SubmissionQuizSerializer,
    CourseDetailSerializer
)
from .permissions import IsAdminOrTeacherOrReadOnly, IsSolver
from ai.agent import (
    generate_course_plan,
    generate_lesson_plan,
    generate_task_plan
)
from ai.course import CreateCoursePlan


class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrTeacherOrReadOnly]

    def get_serializer_class(self): # type: ignore
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class LessonAPIViews(ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrTeacherOrReadOnly]
    
    def get_queryset(self): # type: ignore
        user = self.request.user
        if user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(course__creator=user)


class TaskAPIViews(ModelViewSet):
    serializer_class = TaskSerializer    
    permission_classes = [IsAdminOrTeacherOrReadOnly]
    
    def get_queryset(self): # type: ignore
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(course__creator=user)
    

class QuizAPIViews(ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAdminOrTeacherOrReadOnly]
    
    def get_queryset(self): # type: ignore
        user = self.request.user
        if user.is_superuser:
            return Quiz.objects.all()
        return Quiz.objects.filter(course__creator=user)


class SubmissionTaskAPIView(ModelViewSet):
    serializer_class = SubmissionTaskSerializer
    permission_classes = [IsSolver]
    
    def get_queryset(self): # type: ignore
        user = self.request.user
        if user.is_superuser:
            return SubmissionTask.objects.all()
        
        if user.is_staff:
            return SubmissionTask.objects.filter(task__course__creator=user)

        return SubmissionTask.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuizOptionAPIView(ModelViewSet):
    serializer_class = QuizOptionSerializer
    permission_classes = [IsAdminOrTeacherOrReadOnly]

    def get_queryset(self): # type: ignore
        user = self.request.user
        if user.is_superuser:
            return QuizOption.objects.all()
        return QuizOption.objects.filter(quiz__course__creator=user)
    
    def create(self, request, *args, **kwargs):
        if not isinstance(request.data, list) or len(request.data) != 4:
            raise ValidationError("You must provide exactly 4 answer options!")
        
        bulk_serializer = self.get_serializer(data=request.data, many=True)
        bulk_serializer.is_valid(raise_exception=True)
        bulk_serializer.save()
        return Response(bulk_serializer.data, status=status.HTTP_201_CREATED)


class AiCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"topic":"text"})
    
    def post(self, request):
        user = request.user
        topic = request.data.get('topic')
        cours = generate_course_plan(topic)
        db_cours = CreateCoursePlan.save_course_plan(cours, user)
        less = generate_lesson_plan(topic)
        CreateCoursePlan.save_lesson_plan(less, db_cours)
        task = generate_task_plan(topic)
        CreateCoursePlan.save_task_plan(task, db_cours)
        
        serializer = CourseDetailSerializer(db_cours)
        return Response(serializer.data)