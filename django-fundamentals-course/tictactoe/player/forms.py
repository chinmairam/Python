from django.forms import ModelForm

from .models import Invitation


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ('from_user', 'timestamp')

#  We use meta class to tell django on which model our form will be based.
