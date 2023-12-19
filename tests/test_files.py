import pytest
from django.utils import timezone
from main.models import File


@pytest.mark.django_db(transaction=True)
def test_files(django_client):
    File.objects.create(
        file='test',
        uploaded_at=timezone.now(),
        processed='False',
    )
    response = django_client.get('/files/')

    assert File.objects.count() == 1
    assert response.status_code == 200
