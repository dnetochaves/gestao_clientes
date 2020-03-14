from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person, Docs
from .forms import PersonForm
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.

@login_required
def start(request):
    #return HttpResponse('start')
    return render(request, 'clientes/start_clientes.html')


def person_list(request):
    person = Person.objects.all()
    return render(request, 'clientes/person_list.html', { 'person': person })


@login_required()
def new_person(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record saved successfully !.')
        return redirect('/clientes/person_list')
    return render(request, 'clientes/new_person.html', {'form': form})   


@login_required
def update_person(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record saved successfully !.')
        return redirect('/clientes/person_list')
    return render(request, 'clientes/new_person.html', {'form': form})   


@login_required
def delete_person(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    messages.success(request, f'{ person.frist_name } excluido')
    return redirect('/clientes/person_list')   

class DocsList(ListView):
    model = Docs
