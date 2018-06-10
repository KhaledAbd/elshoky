from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import MakersForm, ModelsForm


def HomePage(request):
    return render(request, 'factory/index.html', None)


def get_name(request):
    if request.method == 'POST':
        form = MakersForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/maker/')
    else:
        form = MakersForm(request.POST)
        return render(request, 'factory/form.html', {'form': form})


def get_Model(request):
    if request.method == 'POST':
        form = ModelsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/factory/')
    else:
        form = ModelsForm(request.POST)
        return render(request, 'factory/model.html', {'form': form})
