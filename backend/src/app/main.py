from fastapi import FastAPI

from app.api.routes import courses
from app.services.course_service import (
    CourseNotFoundError,
    DuplicateCourseError
)
from app.core.exceptions import (
    course_not_found_handler,
    duplicate_course_handler
)


app = FastAPI(
    title="Mathim API",
    description="Mathematics learning platform",
    version="1.0.0"
)


# Register exception handlers
app.add_exception_handler(
    CourseNotFoundError,
    course_not_found_handler
)

app.add_exception_handler(
    DuplicateCourseError,
    duplicate_course_handler
)


# Register routers
app.include_router(courses.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Mathim API"
    }