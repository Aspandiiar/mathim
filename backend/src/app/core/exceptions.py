from fastapi import Request
from fastapi.responses import JSONResponse

from app.services.course_service import (
    CourseNotFoundError,
    DuplicateCourseError
)


async def course_not_found_handler(
    request: Request,
    exc: CourseNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "code": "COURSE_NOT_FOUND",
            "message": str(exc)
        }
    )


async def duplicate_course_handler(
    request: Request,
    exc: DuplicateCourseError
):
    return JSONResponse(
        status_code=409,
        content={
            "code": "COURSE_ALREADY_EXISTS",
            "message": str(exc)
        }
    )