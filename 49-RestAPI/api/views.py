from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers,models
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    ListCreateAPIView,   # you can with it list and also create a view based on inputs
    RetrieveUpdateAPIView  # it can show a view and also update it with patch method
)

class ArticleListView(ListCreateAPIView):
    serializer_class=serializers.ArticleSerializer
    def get_queryset(self):
        query={}
        for key,value in self.request.GET.items():
            query["{}__icontains".format(key)]=value
        return models.Article.objects.filter(**query)

class ArticleDetailtView(RetrieveUpdateAPIView):
    queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer

