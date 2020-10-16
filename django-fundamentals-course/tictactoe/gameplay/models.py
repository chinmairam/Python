from django.db import models
from django.contrib.auth.models import User


GAME_STATUS_CHOICES = (
    ('F', 'First Player To Move'),
    ('S', 'Second Player To Move'),
    ('W', 'First Palyer Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw')
)


class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="games_first_player",
                                     on_delete=models.CASCADE
                                     )
    second_player = models.ForeignKey(User,
                                      related_name="games_second_player",
                                      on_delete=models.CASCADE
                                      )
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,default='F',
                              choices=GAME_STATUS_CHOICES)

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player)



# Create your models here.


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    by_first_player = models.BooleanField() # who made the move

    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE
                             )
    # blank = True will allow the user to leave the comment field empty
