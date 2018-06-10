app_name ='factory'
from django.urls import path
from .views import *
# Create your views here.
urlpatterns=[
    path('', HomePage, name='Home'),
    path('maker/', get_name, name = 'maker'),
    path('model/', get_Model, name = 'model_form')
]