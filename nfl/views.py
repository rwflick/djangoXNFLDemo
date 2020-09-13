from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from nfl.models import Team, Player

# Create your views here.
class TeamListView(ListView):
    model = Team

class TeamDetailView(DetailView):
    model = Team

class PlayerListView(ListView):
    model = Player
