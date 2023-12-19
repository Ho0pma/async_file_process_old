from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import File
from .serializers import FileSerializer
from .tasks import download_file, make_processed_true


# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['get'])
    def files(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        files = request.FILES.getlist('file')

        for uploaded_file in files:
            # Создаем и сохраняем объект File для каждого файла
            file_obj = File(file=uploaded_file)
            file_obj.save()

            # Запускаем Celery задачу для обработки файла
            download_file.delay(file_obj.id)

            # Меняем processed на True
            make_processed_true.delay(file_obj.id)

        serializer = FileSerializer(File.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
