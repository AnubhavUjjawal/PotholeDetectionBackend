from django.urls import include, path
from .views import PotholeList

urlpatterns = [
    path('view/', PotholeList.as_view()),
]