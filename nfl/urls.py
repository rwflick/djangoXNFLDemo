from django.urls import path, include
from nfl.views import TeamListView, TeamDetailView, PlayerListView

urlpatterns = [
    path('team/list/', TeamListView.as_view(), name='team-list'),
    path('team/detail/<int:pk>', TeamDetailView.as_view(), name='team-detail'),
    path('player/list', PlayerListView.as_view(), name='player-list')
]
