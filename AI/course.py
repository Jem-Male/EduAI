from .schemas import (
    CoursePlan, 
    LessonPlan,
    TaskPlan,
    QuizPlan,
    QuizOptionPlan
)
from courses.models import (
    Course, 
    Lesson,
    Task,
    Quiz,
    QuizOption
)

class CreateCoursePlan():
    @classmethod
    def save_course_plan(cls, plan: CoursePlan, user) -> Course:
        return Course.objects.create(
            title=plan.title,
            description=plan.description,
            creator=user,
            ai_course=True,
        )

    @classmethod
    def save_lesson_plan(cls, plan: LessonPlan, course: Course) -> Lesson:
        return Lesson.objects.create(
            course=course,
            title=plan.title,
            description=plan.description
        )
    
    @classmethod
    def save_task_plan(cls, plan: TaskPlan, course: Course) -> Task:
        return Task.objects.create(
            course=course,
            title=plan.title,
            question_text=plan.question_text
        )