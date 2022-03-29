from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
@api_view(["GET"])
def lecture(request, id):
    content = models.Content.objects.filter(lecture_id=id)
    serializer = serializers.ContentSerializer(content, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
