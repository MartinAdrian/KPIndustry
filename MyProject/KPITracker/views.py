import datetime

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.apps import apps
from .models import *


class HomeView(LoginRequiredMixin, ListView):

    model = UserList
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = self.model.objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context


class CreateUserView(LoginRequiredMixin, CreateView):

    model = UserList
    fields = ["first_name", "last_name", "email", "username", "password", "user_type"]
    template_name = "KPITracker/userIndex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        context["users"] = self.model.objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
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


class CreateProjectsView(LoginRequiredMixin, CreateView):

    model = Projects
    fields = ["project_name", "project_partner", "project_manager", "active"]
    template_name = "KPITracker/projectsIndex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-projects")


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = UserList
    fields = ["first_name", "last_name", "email", "username", "user_type"]
    template_name = "KPITracker/userUpdate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-users")


@login_required
def finish_project(request, pk):
    Projects.objects.filter(id=pk, end_date=None).update(active=False)
    Projects.objects.filter(id=pk, end_date=None).update(project_activity="Finished")
    Projects.objects.filter(id=pk, end_date=None).update(end_date=datetime.datetime.now())

    return redirect("KPIndustry:manage-projects")


@login_required
def reopen_project(request, pk):
    Projects.objects.filter(id=pk, start_date=None).update(active=True)
    Projects.objects.filter(id=pk, start_date=None).update(project_activity="Ongoing")
    Projects.objects.filter(id=pk, start_date=None).update(start_date=datetime.datetime.now())

    return redirect("KPIndustry:manage-projects")


class UpdateProjectView(LoginRequiredMixin, UpdateView):

    model = Projects
    fields = ["project_name", "project_partner", "project_manager"]
    template_name = "KPITracker/projectUpdate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-projects")


class ViewProjects(LoginRequiredMixin, ListView):

    model = Projects
    template_name = "KPITracker/projectManagement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context