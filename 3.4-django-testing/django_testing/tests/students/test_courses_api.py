import pytest
from model_bakery import baker
from students.models import Course, Student

@pytest.mark.django_db
def test_first_course(client, user, students_factory, courses_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=10, students=students)

    first_course = Course.objects.all().first()

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

    filtered_course = Course.objects.filter(id=24).first()

    response = client.get('/courses/')
    data = response.json()

    assert data[2]['id'] == filtered_course.id

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
    response_delete = client.delete('/courses/43/')

    assert response_delete.status_code == 204

