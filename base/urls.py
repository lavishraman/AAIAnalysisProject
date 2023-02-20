from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-project/',views.createProject, name="create-project"),
    path('update-project/<str:pk>/',views.updateProject, name ="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject, name ="delete-project"),

]