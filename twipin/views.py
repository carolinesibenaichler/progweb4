from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Twip
from django.views.decorators.csrf import csrf_exempt

def index(request):
   contexto = {} 
   return render(request, 'twipin/index.html', contexto)

@csrf_exempt
def api_twips(request):
  if request.method == "GET" :
    twips = Twip.objects.all()
    jt =  {"lista":[]} 
    for t in twips:
      temp = {"id": t.id, "texto": t.texto, "autor":t.autor.username}
      jt ["lista"].append(temp)
    return JsonResponse(jt)
  elif request.method == "POST":
    t = request.POST["texto"]
    #salva no banco
    usuario = User.objects.get(username='admin')
    twip = Twip(autor = usuario, texto = t)
    twip.save()  
    jt = { "mensagem": "ok"}
    return JsonResponse(jt)
