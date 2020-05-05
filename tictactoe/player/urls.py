from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, SignUpView

urlpatterns = [
    url('home/', home, name="player_home"),
    url('login/',
        LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),
    url('logout/',
        LogoutView.as_view(),
        name="player_logout"),
    url('new_invitation/', new_invitation, name="player_new_invitation"),
    url('accept_invitation/(?P<id>\d+)/$', accept_invitation,
        name="player_accept_invitation"),
    url('signup/', SignUpView.as_view(), name='player_signup'),
]