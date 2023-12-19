import pytest
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture(scope='session')
def django_client():
    # Инициализация тестового клиента Django
    client = Client()
    return client


@pytest.fixture
def test_image_files(tmpdir):
    file_content = b'Test image content'
    files = [
        SimpleUploadedFile("test_image1.jpg", file_content),
        SimpleUploadedFile("test_image2.jpg", file_content),
    ]
    return files
