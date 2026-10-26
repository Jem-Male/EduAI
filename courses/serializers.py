from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max 
from rest_framework import serializers
from .models import Course, Lesson, Task, Quiz, QuizOption, SubmissionTask, SubmissionQuiz


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'position', 'title', 'description', 'image', 'video', 'created_at']
        read_only_fields = ['position', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'course', 'position', 'title', 'question_text', 'image', 'video', 'created_at']
        read_only_fields = ['position', 'created_at']


class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = ['id', 'quiz', 'options_test', 'is_correct', 'feedback', 'created_at']
        read_only_fields = ['created_at']
        
        extra_kwargs = {'is_correct': {'write_only': True}}


class QuizSerializer(serializers.ModelSerializer):
    options = QuizOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'position', 'answer', 'question_text', 'options', 'created_at']
        read_only_fields = ['position', 'created_at']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'creater', 'created_at']
        read_only_fields = ['creater', 'created_at']


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'image', 'creater', 
            'lessons', 'tasks', 'quizzes', 'created_at'
        ]
        read_only_fields = ['creater', 'created_at']


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