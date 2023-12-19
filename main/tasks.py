from celery import shared_task
from main.models import File


@shared_task
def download_file(file_id):
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = False
    file_instance.save()


@shared_task
def make_processed_true(file_id):
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_instance.save()
