from django.views.generic import ListView
from django.shortcuts import render
from KPITracker.models import UserList


class UserView(ListView):
    model = UserList
    template_name = "KPITracker/userIndex.html"
