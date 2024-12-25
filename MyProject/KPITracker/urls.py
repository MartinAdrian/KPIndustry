from django.urls import path
from KPITracker import views

app_name = "KPIndustry"

urlpatterns = [
    path("", views.UserView.as_view(), name="userscreen"),
    path("add-user/", views.UserView.as_view(), name="add-user"),
]