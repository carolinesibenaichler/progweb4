from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('api/twips', views.api_twips, name= 'api_twips')
]
