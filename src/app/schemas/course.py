
from typing import Literal

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator,
    model_validator
)


class CourseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=10, max_length=500)

    difficulty: Literal[
        "beginner",
        "intermediate",
        "advanced"
    ]

    @field_validator("title", "description")
    @classmethod
    def strip_whitespace(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")

        return value


class CourseUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        min_length=10,
        max_length=500
    )

    difficulty: Literal[
        "beginner",
        "intermediate",
        "advanced"
    ] | None = None

    @field_validator("title", "description")
    @classmethod
    def strip_whitespace(cls, value):
        if value is None:
            return value

        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")

        return value

    @model_validator(mode="after")
    def validate_update(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")

        for field in self.model_fields_set:
            if getattr(self, field) is None:
                raise ValueError(f"{field} cannot be null")

        return self


class CourseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    difficulty: str
