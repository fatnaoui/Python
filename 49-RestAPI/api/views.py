from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers,models
from rest_framework.generics import RetrieveAPIView,ListAPIView

class ArticleListView(ListAPIView):
    queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer

class ArticDetailtView(RetrieveAPIView):
    queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer

