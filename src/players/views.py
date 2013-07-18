from django.shortcuts import render, get_object_or_404

from players.models import Player

def index(request):
    players_list = Player.objects.all().order_by('last_name')
    context = {'players_list': players_list}
    return render(request, 'players/index.html', context)

def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    age = player.age()
    age_in_years = age.days // 365
    context = {'player': player, 'age': age_in_years}
    return render(request, 'players/player.html', context)

