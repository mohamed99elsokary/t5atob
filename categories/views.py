from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
@api_view(["GET"])
def categories(request):
    categories = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
