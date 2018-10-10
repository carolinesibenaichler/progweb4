from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Twip

def index(request):
   contexto = {} 
   return render(request, 'twipin/index.html', contexto)


def api_twips(request):
  if request.method == "GET" :
    twips = Twip.objects.all()
    jt =  {"lista":[]} 
    for t in twips:
      temp = {"id": t.id, "texto": t.texto, "autor":t.autor.username}
      jt ["lista"].append(temp)
    return JsonResponse(jt)
  elif request.method == "POST":
    #TODO salvar no baco
    jt = { "resposta": "ok"}
    return JsonResponse(jt)
