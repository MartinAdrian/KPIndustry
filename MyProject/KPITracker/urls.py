from django.urls import path
from KPITracker import views

app_name = "KPIndustry"

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("view-users/", views.CreateUserView.as_view(), name="view-users"),
    path("view-users/", views.UserView.as_view(), name="view-users"),
]