import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from django_testing import settings
from students.models import Course, Student
from django.contrib.auth.models import User
@pytest.fixture
def user():
    return User.objects.create_user('admin')

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses_factory():

    def factory(*args, **kwargs):
        courses = baker.make(Course, *args, **kwargs)
        return courses
    return factory

@pytest.fixture
def limit_quantity(settings):
    settings.MAX_STUDENTS_PER_COURSE = True
    assert settings.MAX_STUDENTS_PER_COURSE

@pytest.fixture
def students_factory():

    def factory(*args, **kwargs):
        students = baker.make(Student, *args, **kwargs)
        return students

    return factory
