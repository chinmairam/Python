from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation

urlpatterns = [
    path('home', home, name="player_home"),
    path('login',
         LoginView.as_view(template_name="player/login_form.html"),
         name="player_login"),
    path('logout',
         LogoutView.as_view(),
         name="player_logout"),
    path('new_invitation', new_invitation, name="player_new_invitation")
]

# as_view() converts Logout(class of another Function) to Function.
