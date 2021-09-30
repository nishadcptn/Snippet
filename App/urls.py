from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

urlpatterns = [
    path('token', TokenObtainPairView.as_view()),       # Token generating Api
    path('token/refresh', TokenRefreshView.as_view()),  # for getting refresh token
    path('snippet/', SnippetApi.as_view()),             # for getting snippet and all snippe count / creating snippet/ 
    path('snippet/<int:pk>', SnippetApi.as_view()),     # for getting snippet details with pk / updating snippets / deleting Snippets
    path('tag/', TagApi.as_view()),                     # for getting snippet and all tag names / Snippet linked to tag (POST method) {'tag':'name'}
]