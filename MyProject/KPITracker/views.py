from django import forms
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import render
from .models import UserList

class HomeView(ListView):

    model = UserList
    template_name = "base.html"


class UserView(ListView):

    model = UserList
    template_name = "KPITracker/userIndex.html"


class CreateUserView(CreateView):

    model = UserList
    fields = ["FirstName", "LastName", "eMail", "Username", "UserType"]
    template_name = "KPITracker/userIndex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:view-users")


class ManageUserView(UpdateView):

    model = UserList
    template_name = "KPITracker/userIndex.html"