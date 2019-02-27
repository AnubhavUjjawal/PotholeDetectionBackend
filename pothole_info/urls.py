from django.urls import include, path
from .views import PotholeList

urlpatterns = [
    path('view/<int:pk>/', PotholeList.as_view(), name="PotholeList"),
    path('view/', PotholeList.as_view(), name="PotholeList"),
]