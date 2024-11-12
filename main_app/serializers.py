from rest_framework import serializers
from .models import Cat, Feeding

class CatSerializer(serializers.ModelSerializer) :
    class Meta: 
        model = Cat
        fields = '__all__'

class FeedingSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('cat',)