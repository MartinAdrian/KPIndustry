from django.urls import path
from KPITracker import views

app_name = "KPIndustry"

urlspatterns = [
    path("", views.UserView.as_view(), name="userscreen"),
]