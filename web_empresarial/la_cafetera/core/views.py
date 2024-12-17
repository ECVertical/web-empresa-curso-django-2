from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, "core/inicio.html")

def historia(request):
    return render(request, "core/historia.html")

def visitanos(request):
    return render(request, "core/visitanos.html")

