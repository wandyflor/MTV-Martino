from asyncio import run_coroutine_threadsafe
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader


# Create your views here.

from AppFamilia.models import Familiar


def crear_familiar(request):
    template = loader.get_template("template1.html")

    primer_familiar = Familiar(nombre = "Lionel", apellido = "Martin", fecha_nacimiento = "1987-08-30", edad = 35, email = "lio@mail.com")
    segundo_familiar = Familiar(nombre = "Clara", apellido = "Lopez", fecha_nacimiento = "1987-07-01", edad = 35, email = "clari@mail.com")
    tercer_familiar = Familiar(nombre = "Rosa", apellido = "Martin", fecha_nacimiento = "1980-01-31", edad = 42, email = "rosi@mail.com")
    
    primer_familiar.save()
    segundo_familiar.save()
    tercer_familiar.save()


    dict_de_contexto = {
        "familiar_1": primer_familiar, 
        "familiar_2": segundo_familiar,
        "familiar_3": tercer_familiar, 
    }


    res = template.render(dict_de_contexto)


    return HttpResponse(res)


def mostrar_inicio(request):
    return render(request, "AppFamilia.html")


    
