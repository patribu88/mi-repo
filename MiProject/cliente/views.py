from django.shortcuts import render

# Create your views here.

app_name = 'cliente'

def index(request):
    return render(request, 'cliente/index_cliente.html')