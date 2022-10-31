import re
from django.shortcuts import redirect, render
from app.forms.forms import PersonForm
from app.models.models import Person

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Person.objects.filter(Name__icontains=search)
    else:
        data['db'] = Person.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    data['form'] = PersonForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Person.objects.get(pk=pk)
    db.delete()
    return redirect('home')

