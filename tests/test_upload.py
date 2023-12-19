import pytest
from main.tasks import download_file, make_processed_true
from unittest.mock import patch, MagicMock


@pytest.mark.django_db
@patch('main.tasks.download_file.delay', MagicMock())
@patch('main.tasks.make_processed_true.delay', MagicMock())
def test_upload(test_image_files, django_client):
    files = {'file': [file for file in test_image_files]}
    response = django_client.post('http://127.0.0.1:8000/upload/', files, format='multipart')

    assert response.status_code == 201
    assert len(response.data) == len(test_image_files)

    for file_data in response.data:
        assert 'id' in file_data
        assert 'processed' in file_data

        # Проверяем, что задачи Celery были вызваны
        download_file.delay.assert_any_call(file_data['id'])
        make_processed_true.delay.assert_any_call(file_data['id'])
