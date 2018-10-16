from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Twip, Curtida
from django.views.decorators.csrf import csrf_exempt

def index(request):
   contexto = {} 
   return render(request, 'twipin/index.html', contexto)

@csrf_exempt
def api_twips_id(request, id):
  if request.method == "DELETE":
   #TODO deletar no banco
    twip = Twip.objects.get(id=id)
    twip.delete()
    
    jt = { "mensagem": "ok"}
    return JsonResponse(jt)


@csrf_exempt
def api_twips(request):
  if request.method == "GET" :
    twips = Twip.objects.all()
    u = User.objects.get(username = 'admin')
    jt =  {"lista":[]} 

    for t in twips:
      curtiu = t.curtida_set.filter(autor_id = u.id).count() > 0
      temp = {"id": t.id, "texto": t.texto, "autor":t.autor.username, "curtidas":t.curtida_set.count(),"curtiu":curtiu}
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
@csrf_exempt
def api_coracao(request, id):
  curtidas = 0 
  if request.method == "POST":
    twip = Twip.objects.get(id = id)
    autor = User.objects.get(username='admin')
    curtida = Curtida(autor = autor, twip = twip)
    curtida.save()
    curtidas = twip.curtida_set.count() 

  elif request.method == "DELETE":
    twip = Twip.objects.get(id = id)
    autor = User.objects.get(username='admin')
    curtida= Curtida.objects.filter(autor = autor, twip = twip)
    curtida.delete()
    curtidas = twip.curtida_set.count() 
  jt = {"curtidas": curtidas}
  return JsonResponse(jt) 