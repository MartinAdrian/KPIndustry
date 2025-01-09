from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import UserList

class HomeView(LoginRequiredMixin, ListView):

    model = UserList
    template_name = "homepage.html"


class CreateUserView(LoginRequiredMixin, CreateView):

    model = UserList
    fields = ["first_name", "last_name", "email", "username", "password", "user_type"]
    template_name = "KPITracker/userIndex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-users")


class ManageUserView(LoginRequiredMixin, UpdateView):

    model = UserList
    template_name = "KPITracker/userIndex.html"


@login_required
def deactivate_user(request, pk):
    UserList.objects.filter(id=pk).update(is_active=False)

    return redirect("KPIndustry:manage-users")


@login_required
def reactivate_user(request, pk):
    UserList.objects.filter(id=pk).update(is_active=True)

    return redirect("KPIndustry:manage-users")