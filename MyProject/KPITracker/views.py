from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import render
from .models import UserList

class HomeView(LoginRequiredMixin, ListView):

    model = UserList
    template_name = "homepage.html"


class UserView(LoginRequiredMixin, ListView):

    model = UserList
    template_name = "KPITracker/userIndex.html"


class CreateUserView(LoginRequiredMixin, CreateView):

    model = UserList
    fields = ["first_name", "last_name", "email", "username", "UserType"]
    template_name = "KPITracker/userIndex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:view-users")


class ManageUserView(LoginRequiredMixin, UpdateView):

    model = UserList
    template_name = "KPITracker/userIndex.html"