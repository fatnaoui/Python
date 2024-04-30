from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
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
    return HttpResponse(json.dumps(users),content_type='application/json')

