

from django.shortcuts import render

def index (request):
    return render (request, 'index.html',
                   {
                       'titulo_empresa' : 'Natural Star'
                   })