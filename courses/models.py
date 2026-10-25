from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max 


class AnswerResult(models.TextChoices):
    WRONG = 'wrong', 'Incorrect'
    PARTIALLY_CORRECT = 'partially', 'Partially Correct'
    CORRECT = 'correct', 'Correct'


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name="Course name")
    description = models.TextField(verbose_name="Course deconstruct")
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    position = models.PositiveIntegerField(default=0, editable=False)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='lessons/images/', null=True, blank=True)
    video = models.FileField(upload_to='lessons/video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.position:
            max_position = Lesson.objects.filter(course=self.course).aggregate(Max('position'))['position__max']
            self.position = (max_position or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')
    position = models.PositiveIntegerField(default=0, editable=False)
    title = models.CharField(max_length=200)
    question_text = models.TextField()
    image = models.ImageField(upload_to='tasks/images/', null=True, blank=True)
    video = models.FileField(upload_to='tasks/video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
        
    def save(self, *args, **kwargs):
        if not self.position:
            max_position = Lesson.objects.filter(course=self.course).aggregate(Max('position'))['position__max']
            self.position = (max_position or 0) + 1    
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Task: {self.title}"


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    position = models.PositiveIntegerField(default=0, editable=False)
    answer = models.CharField(max_length=200)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

        
    def save(self, *args, **kwargs):
        if not self.position:
            max_position = Lesson.objects.filter(course=self.course).aggregate(Max('position'))['position__max']
            self.position = (max_position or 0) + 1            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Quiz: {self.question_text}"


class SubmissionTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student_answer = models.TextField()
    
    answer_result = models.CharField(
        max_length=20,
        choices=AnswerResult.choices,
        null=True,
        blank=True,
        verbose_name="Результат ответа"
    )
    ai_feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task.title} ({self.answer_result})"


class QuizOption(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='options')
    options_test = models.CharField(max_length=150, verbose_name="Option Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is Correct?")
    ai_feedback = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quiz}"


class SubmissionQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student_answer = models.ForeignKey(QuizOption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.answer} ({self.student_answer.is_correct})"