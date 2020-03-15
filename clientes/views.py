from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person, Docs
from .forms import PersonForm
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def start(request):
    #return HttpResponse('start')
    time = timezone.now()
    return render(request, 'clientes/start_clientes.html', {'time': time})


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DocsDetail(DetailView):

    model = Docs


class DocsCreate(CreateView):
    model = Docs
    fields = ['type_name', 'note']
    success_url = 'docs_list'

class DocsUpdate(UpdateView):
    model = Docs
    fields = ['type_name', 'note']
    success_url = reverse_lazy('docs_list')


class DocsDelete(DeleteView):
    model = Docs

    def get_success_url(self):
        return reverse_lazy('docs_list')
    
