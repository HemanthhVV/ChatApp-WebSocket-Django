from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("", views.index,name = "chat-page"),
    path("auth/login",LoginView.as_view(
        template_name = "chat/loginpage.html"
    ),name = "login-user"),
    path("auth/logout",LogoutView.as_view(),name = "logout-user"),
]