from rest_framework import serializers
from . import models


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecture
        fields = "__all__"
