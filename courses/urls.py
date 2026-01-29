from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
     path('', views.course_list, name='course_list'), 
     path('created/', views.course_create, name='create'),
     path('<int:id>/', views.course_detail, name='detail'),
     path('<int:id>/edit/', views.course_edit, name='edit'),
     path('<int:id>/delete', views.course_delete, name='delete'),
]
