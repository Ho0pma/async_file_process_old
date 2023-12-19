import os

from django.db import models


def file_upload_path(instance, filename):
    # Эта функция генерирует путь для сохранения файла
    return os.path.join('media', filename)


class File(models.Model):
    file = models.FileField(upload_to=file_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.file.name} - {self.uploaded_at} - Processed: {self.processed}'
