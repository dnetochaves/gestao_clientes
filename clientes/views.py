from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def start(request):
    #return HttpResponse('start')
    return render(request, 'clientes/start_clientes.html')
