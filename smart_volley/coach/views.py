from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from .models import Coach


class CoachCreateView(CreateView):
    model = Coach
    fields = ['name']
    
    def post(self, request):
        return HttpResponse('Creando Coach')


class CoachListView(ListView):
    model = Coach