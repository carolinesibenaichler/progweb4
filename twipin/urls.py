from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('api/twips', views.api_twips, name= 'api_twips'),
    path('api/twips/<int:id>', views.api_twips_id, name= 'api_twips_id')
]
