from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.shortcuts import render
from KPITracker.models import UserList


class UserView(ListView):
    model = UserList
    template_name = "KPITracker/userIndex.html"

class CreateUserView(CreateView):
    model = UserList
    fields = ["FirstName", "LastName","eMail","UserType"]
    template_name = "KPITracker/addUserForm.html"

    def get_success_url(self):
        return reverse("KPITracker/userscreen")