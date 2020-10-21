from django.shortcuts import render

from gameplay.models import Game


# Create your views here.


def home(request):
    """games_first_player = Game.objects.filter(
        first_player=request.user,
        status='F'
    )
    games_second_player = Game.objects.filter(
        second_player=request.user,
        status='S'
    )
    all_my_games = list(games_first_player) + \
                   list(games_second_player)

    return render(request, "player/home.html",
                  {'games': all_my_games})
    # {'ngames': Game.objects.count()})"""
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})

# render means instead of immediately returning the response,
#   we want the view to delegate(give) the actual generation
#   of the html page to the template.
#  arguments: request object, template
