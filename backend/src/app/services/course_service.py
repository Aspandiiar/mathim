courses = {}
next_id = 1


class CourseNotFoundError(Exception):
    pass


class DuplicateCourseError(Exception):
    pass


def get_all_courses():
    return list(courses.values())


def get_course(course_id: int):

    course = courses.get(course_id)

    if course is None:
        raise CourseNotFoundError(
            f"Course {course_id} not found"
        )

    return course


def create_course(course_data: dict):

    global next_id

    # Business rule: unique course titles
    for course in courses.values():
        if course["title"].lower() == course_data["title"].lower():
            raise DuplicateCourseError(
                "Course already exists"
            )

    new_course = {
        "id": next_id,
        **course_data
    }

    courses[next_id] = new_course
    next_id += 1

    return new_course


def update_course(course_id: int, updates: dict):

    course = get_course(course_id)

    if "title" in updates:
        for existing in courses.values():

            if (
                existing["title"].lower() == updates["title"].lower()
                and existing["id"] != course_id
            ):
                raise DuplicateCourseError(
                    "Course title already exists"
                )

    course.update(updates)

    return course


def delete_course(course_id: int):

    course = get_course(course_id)

    del courses[course_id]

    return course