from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Disciplina, OlimpijskeIgre, Drzava, Tekmovalec

class HomePageView(generic.base.TemplateView):
    template_name = 'olympic_games/home.html'

class ResultsPageView(generic.edit.FormMixin):
    template_name = 'olympic_games/search.html'







    

