from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Task,
    Quiz,
    QuizOption,
    SubmissionTask,
    SubmissionQuiz
)

admin.site.register(Course)
admin.site.register(Lesson)