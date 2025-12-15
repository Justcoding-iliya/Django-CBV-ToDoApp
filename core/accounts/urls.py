from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
]