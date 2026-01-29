# 1 Studentlar ro'yxati
from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_list'),
    path('<int:id>/', views.student_detail, name='student_detail'),
]
