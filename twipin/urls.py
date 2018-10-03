from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('json/exemplo', views.json_exemplo, name='json_exemplo'),  
]
