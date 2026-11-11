from rest_framework import serializers
from .models import Course, Lesson, Task, Quiz, QuizOption, SubmissionTask, SubmissionQuiz
from rest_framework.exceptions import ValidationError


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'position', 'title', 'description', 'image', 'video', 'created_at']
        read_only_fields = ['position', 'created_at']
    
    def validate_course(self, value):
        user = self.context['request'].user
        if value.creator != user and not user.is_superuser:
            raise ValidationError("You cannot add lessons to someone else's course!")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'course', 'position', 'title', 'question_text', 'image', 'video', 'created_at']
        read_only_fields = ['position', 'created_at']
    
    def validate_course(self, value):
        user = self.context['request'].user
        if value.creator != user and not user.is_superuser:
            raise ValidationError("You cannot add tasks to someone else's course!")
        return value


class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = ['id', 'quiz', 'options_test', 'is_correct', 'feedback', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {'is_correct': {'write_only': True}}
        
    def validate_quiz(self, value):
        user = self.context['request'].user
        if value.course.creator != user and not user.is_superuser:
            raise ValidationError("You cannot add options to someone else's quiz!")
        return value


class QuizSerializer(serializers.ModelSerializer):
    options = QuizOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'position', 'answer', 'question_text', 'options', 'created_at']
        read_only_fields = ['position', 'created_at']
    
    def validate_course(self, value):
        user = self.context['request'].user
        if value.creator != user and not user.is_superuser:
            raise ValidationError("You cannot add quizzes to someone else's course!")
        return value


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'creator', 'created_at']
        read_only_fields = ['creator', 'created_at']


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'image', 'creator', 
            'lessons', 'tasks', 'quizzes', 'created_at'
        ]
        read_only_fields = ['creator', 'created_at']


class SubmissionTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionTask
        fields = ['id', 'user', 'task', 'student_answer', 'answer_result', 'ai_feedback', 'created_at']
        read_only_fields = ['user', 'answer_result', 'ai_feedback', 'created_at']


class SubmissionQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionQuiz
        fields = ['id', 'user', 'quiz', 'student_answer', 'created_at']
        read_only_fields = ['user', 'created_at']
    

class CourseRequestSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=300)