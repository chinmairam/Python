from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .models import Invitation
from gameplay.models import Game


# Create your views here.

@login_required()
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


@login_required
def new_invitation(request):
    if request.method == "POST":
        #  TODO handle form submit
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
        return render(request, "player/new_invitation_form.html", {'form': form})
# render means instead of immediately returning the response,
#   we want the view to delegate(give) the actual generation
#   of the html page to the template.
#  arguments: request object, template
