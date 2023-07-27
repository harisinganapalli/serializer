from rest_framework import serializers
from .models import *


class StudentSerializers(serializers.Serializer):
    class Meta:
        model=Student
        fields="__all__"