from rest_framework import serializers

from .models import (
    Course,
    Lesson,
    Task,
    Quiz,
    SubmissionQuiz,
    SubmissionTask,
    QuizOption,
)


class CourseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Course
        field = ["id", "title", "description", "creater", "created_at"]
        
        