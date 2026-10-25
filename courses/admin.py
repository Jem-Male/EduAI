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


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    readonly_fields = ('position',) 

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1

class QuizOptionInline(admin.TabularInline):
    model = QuizOption
    extra = 4


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'creater', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'creater')
    inlines = [LessonInline, TaskInline, QuizInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'created_at')
    inlines = [QuizOptionInline]


@admin.register(SubmissionTask)
class SubmissionTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'answer_result', 'created_at')
    list_filter = ('answer_result', 'created_at')
    search_fields = ('user__username', 'task__title')


@admin.register(SubmissionQuiz)
class SubmissionQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'created_at')
    search_fields = ('user__username', 'quiz__question_text')