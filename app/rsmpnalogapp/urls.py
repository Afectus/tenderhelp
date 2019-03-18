from django.contrib import admin
from django.urls import path
from .views import Check_business_entity


urlpatterns = [
    path('check_business_entity/', Check_business_entity.as_view(), name='check_business_entity'  ),
]
