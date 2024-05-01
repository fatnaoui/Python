from django.urls import path
from api import views
urlpatterns=[
    path('apiarticle/',views.apiarticle),
    path('users/',views.usersApi)
]