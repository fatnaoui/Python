from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
@api_view()
def usersApi(request):
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
    return Response(users)

