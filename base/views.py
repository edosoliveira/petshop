from django.shortcuts import render

def inicio (request):
   return render (request, 'inicio.html') # aqui eu chamo a pagina html que esta no templates 
def contato (request):
    return render (request, 'contato.html')