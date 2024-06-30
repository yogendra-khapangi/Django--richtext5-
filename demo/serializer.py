from rest_framework import serializers
from .models import *


class SudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactModel
        fields = '__all__'