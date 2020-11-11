from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from web_api.views import HelloWorldView, RegisterApi


urlpatterns = [
    path('hello_world/', HelloWorldView.as_view()),
    path('register/', RegisterApi.as_view()),
]
