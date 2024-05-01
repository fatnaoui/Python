from rest_framework import serializers
from api import models

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    id=serializers.IntegerField()
    mark=serializers.IntegerField()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True,read_only=True)
    class Meta:
        model=models.Article
        fields='__all__'
