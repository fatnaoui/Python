from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


class Student:
    name="hamza"
    id="1"
    mark=100
# Create your views here.
@api_view()
def usersApi(request):
    student=Student()
    users=[
        {
            "name":"hamza",
            "language":"python"
        },
        {
            "name":"billal",
            "language":"C++"
        }
    ]
    return Response(student)

