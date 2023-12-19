from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    # processed = serializers.HiddenField(default=False)

    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
