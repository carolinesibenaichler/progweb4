from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Twip

def index(request):
   contexto = {} 
   return render(request, 'twipin/index.html', contexto)


def json_exemplo(request):
   
   

   pessoa = {
       "nome": "João",
       "idade": 18,
       "parentes": {
           "mãe": "Maria",
           "pai": "Pedro",
           "irmãos": 2
       }
   }

   return JsonResponse(pessoa)


def json_listar_twips(request):
  twips = Twip.objects.all()

  jt =  {"lista":[]} 
  for t in twips:
     temp = {"id": t.id, "texto": t.texto, "autor":t.autor.username}
     jt ["lista"].append(temp)

  return JsonResponse(jt)
    
