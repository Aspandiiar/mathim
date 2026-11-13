from fastapi import APIRouter, status

from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

from app.services import course_service


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/", response_model=list[CourseResponse])
async def get_courses():

    return course_service.get_all_courses()


@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int):

    return course_service.get_course(course_id)


@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(course: CourseCreate):

    return course_service.create_course(
        course.model_dump()
    )


@router.patch(
    "/{course_id}",
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseUpdate
):

    updates = course.model_dump(exclude_unset=True)

    if not updates:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail="At least one field must be provided"
        )

    if any(value is None for value in updates.values()):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail="Fields cannot be null"
        )

    return course_service.update_course(
        course_id,
        updates
    )


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(course_id: int):

    course_service.delete_course(course_id)