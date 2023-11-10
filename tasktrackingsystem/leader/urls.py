from django.urls import path
from . import views

app_name = 'leader'

urlpatterns = [
    path('add/', views.leader_add, name='leader_add'),

]

