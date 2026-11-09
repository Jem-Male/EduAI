from pydantic import BaseModel, Field, AfterValidator
from typing import Annotated


class CoursePlan(BaseModel):
    title: Annotated[str, Field(max_length=250)]
    description: str


class LessonPlan(BaseModel):
    title: Annotated[str, Field(max_length=250)]
    description: str


class TaskPlan(BaseModel):
    title: Annotated[str, Field(max_length=200)]
    question_text: str


class QuizOptionPlan(BaseModel):
    option_text: Annotated[str, Field(max_length=150)]
    is_correct: bool = False
    feedback: Annotated[str, Field(max_length=250)] | None = None


def check_one_correct(options: list[QuizOptionPlan]) -> list[QuizOptionPlan]:
    if sum(o.is_correct for o in options) != 1:
        raise ValueError('There needs to be exactly one correct option.')
    return options


QuizOptionsList = Annotated[
    list[QuizOptionPlan],
    Field(min_length=4, max_length=4),
    AfterValidator(check_one_correct),
]


class QuizPlan(BaseModel):
    question_text: str
    options: QuizOptionsList