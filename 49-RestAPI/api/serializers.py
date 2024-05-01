from rest_framework import serializers
from api import models

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    id=serializers.IntegerField()
    mark=serializers.IntegerField()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        field='__all__'
