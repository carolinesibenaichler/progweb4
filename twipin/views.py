from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Twip,Curtida
from .forms import FormEntrar
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout, login

def index(request):
   if not request.user.is_authenticated: 
      return HttpResponseRedirect('entrar') 

   contexto = {} 
   return render(request, 'twipin/index.html', contexto)


def entrar(request):
   contexto = {} 
   if request.method == 'POST':
      form = FormEntrar(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         usuario = authenticate(request, username=username, password=password)
         if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/') 
         
   form = FormEntrar() 
   contexto = {"form": form}
   return render(request, 'twipin/entrar.html', contexto)


def sair(request):
   logout(request)
   return HttpResponseRedirect('/') 


@csrf_exempt
def api_twips_id(request, id):
    if request.method == "DELETE":
      twip = Twip.objects.get(id=id)
      twip.delete()

      jt = {"mensagem": "ok"}
      return JsonResponse(jt)

@csrf_exempt
def api_coracao(request, id):

    c = 0 #número de curtidas

    if request.method == "POST":
      t = Twip.objects.get(id=id)
      u = request.user 
      curtida = Curtida(autor=u, twip=t)
      curtida.save()
      c = t.curtida_set.count()
    elif request.method == "DELETE":
      t = Twip.objects.get(id=id)
      u = request.user 
      curtida = Curtida.objects.get(autor=u, twip=t)
      curtida.delete()
      c = t.curtida_set.count()

    jt = {"mensagem": "ok", "curtidas": c}
    return JsonResponse(jt)

@csrf_exempt
def api_twips(request):
   if request.method == "GET":
      twips = Twip.objects.all()
      u = request.user 

      jt = {"lista":[]} 

      for t in twips:
         curtiu = t.curtida_set.filter(autor_id = u.id).count() > 0
         temp = {"id": t.id, "texto": t.texto, "nome":t.autor.first_name, "autor": t.autor.username, "curtidas": t.curtida_set.count(), "curtiu": curtiu, "lat":t.lat, "lng": t.lng}
         jt["lista"].append(temp)   
       
      return JsonResponse(jt)
   elif request.method == "POST":

      #Salva no banco
      t = request.POST["texto"]
      lat = request.POST["lat"]
      lng = request.POST["lng"]
      u = request.user 
      twip = Twip(autor=u, texto = t, lat = lat, lng= lng)
      twip.save()
      
      jt = {"mensagem": "ok", "id": twip.id, "usuario": u.username, "nome": u.first_name}
      return JsonResponse(jt)
 
