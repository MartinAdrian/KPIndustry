from django.contrib.auth.views import LoginView
from django.urls import path, include
from KPITracker import views

app_name = "KPIndustry"

urlpatterns = [
    path("", include("django.contrib.auth.urls"), {"next_page": "/"}, name="login"),
    path("", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("home/", views.HomeView.as_view(), name="homepage"),
    path("manage-users/", views.CreateUserView.as_view(), name="manage-users"),
    path("manage-users/", views.UserView.as_view(), name="manage-users"),
]