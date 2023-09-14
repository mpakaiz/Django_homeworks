import pytest
from model_bakery import baker
from students.models import Course, Student
import random

@pytest.mark.django_db
def test_first_course(client, user, students_factory, courses_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=10, students=students)

    first_course = courses[0]

    response = client.get('/courses/')
    data = response.json()
    assert data[0]['id'] == first_course.id
    assert response.status_code == 200

@pytest.mark.django_db
def test_courses_list(client, user, students_factory, courses_factory, limit_quantity):

    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=10, students=students)

    response = client.get('/courses/')

    data = response.json()
    assert len(data) == len(Course.objects.all())
    assert len(data) == 10

@pytest.mark.django_db
@pytest.mark.xfail
def test_courses_list(client, user, students_factory, courses_factory, limit_quantity):

    students = students_factory(_quantity=11)
    courses = courses_factory(_quantity=11, students=students)

    response = client.get('/courses/')

    data = response.json()
    assert len(data) == len(Course.objects.all())
    assert len(data) == 11

@pytest.mark.django_db
def test_courses_filter_id(client, user, students_factory, courses_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=10, students=students)

    random_course = random.choice(courses)

    response = client.get(f'/courses/{random_course.id}/')
    data = response.json()

    assert data['id'] == random_course.id

@pytest.mark.django_db
def test_courses_filter_name(client, user, students_factory, courses_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=10, students=students)

    filtered_course = Course.objects.filter(name=courses[0].name).first()

    response = client.get('/courses/')
    data = response.json()

    assert data[0]['name'] == filtered_course.name

@pytest.mark.django_db
def test_courses_create(client, user):

    response = client.post('/courses/', data={'name': 'netology'})

    assert response.status_code == 201

@pytest.mark.django_db
def test_courses_delete(client, user):

    response = client.post('/courses/', data={'name': 'netology'})
    created_course_id = response.json()['id']

    response_delete = client.delete(f'/courses/{created_course_id}/')

    assert response_delete.status_code == 204

@pytest.mark.django_db
def test_update_course(client, user):
    response = client.post('/courses/', data={'name': 'netology'})
    created_course_id = response.json()['id']

    response_patch = client.patch(f'/courses/{created_course_id}/', data={'name': 'netology_test'})

    assert response_patch.status_code == 200

    updated_course = Course.objects.get(id=created_course_id)
    assert updated_course.name == 'netology_test'


