from django.urls import path
from . import views

app_name = 'capabilities'

urlpatterns = [
    path('add/', views.capabilities_add, name='add_capabilities'),

]
