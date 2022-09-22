from dataclasses import field
from rest_framework import serializers
from .models import *



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = '__all__'

    def validate(self, data):
        if data['age'] <18:
            raise serializers.ValidationError({'error': "age cannot be less than 18"})
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Category
        field = '__all__'