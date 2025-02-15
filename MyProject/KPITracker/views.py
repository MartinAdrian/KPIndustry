import datetime
import requests
from bs4 import BeautifulSoup
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.base import kwarg_re
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.apps import apps
from .models import *


class HomeView(LoginRequiredMixin, ListView):

    model = UserList
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today_date"] = datetime.date.today().strftime("%d-%m-%Y")
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["users"] = self.model.objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        context["report"] = apps.get_model("KPITracker", "KPIReport").objects.filter(reporter_id=self.request.user.id, report_date=datetime.date.today().strftime("%d-%m-%Y"))
        return context

class CreateUserView(LoginRequiredMixin, CreateView):

    model = UserList
    template_name = "KPITracker/userIndex.html"
    fields = ["first_name", "last_name", "email", "username", "user_type", "gross_salary", "phone_number", "work_location"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name",flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = self.model.objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        password = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*") for _ in range(12))
        user_instance = UserList.objects.get(id=self.object.id)
        user_instance.set_password(password)
        user_instance.save()
        content = (f"Please remember you KPIndustry credentials: \n"
                   f"User: {user_instance.username}\n"
                   f"Password: {password}\n"
                   f"LogIn link: 127.0.0.1:8000/KPIndustry/")
        msg_html = render_to_string("registration/invite_user.html", {"content_email": content})
        email = EmailMultiAlternatives(subject="Date conectare aplicatie", body=content,
                                       from_email="content@test.ro", to=[user_instance.email])
        email.attach_alternative(msg_html, "text/html")
        email.send()
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
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-projects")


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = UserList
    fields = ["first_name", "last_name", "email", "username", "user_type", "gross_salary", "phone_number", "work_location"]
    template_name = "KPITracker/userUpdate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        user_type = self.object.user_type
        user_id = self.object.id
        if not user_type == "Tester" or not user_type == "Lead Tester":
            UserList.objects.filter(id=user_id).update(on_project="None")
        return reverse("KPIndustry:manage-users")


@login_required
def finish_project(request, pk):
    Projects.objects.filter(id=pk, end_date=None).update(active=False)
    Projects.objects.filter(id=pk, end_date=None).update(project_activity="Finished")
    Projects.objects.filter(id=pk, end_date=None).update(end_date=datetime.datetime.now())

    return redirect("KPIndustry:manage-projects")


@login_required
def start_project(request, pk):
    Projects.objects.filter(id=pk, start_date=None).update(project_activity="Ongoing")
    Projects.objects.filter(id=pk, start_date=None).update(start_date=datetime.datetime.now())

    return redirect("KPIndustry:manage-projects")


class UpdateProjectView(LoginRequiredMixin, UpdateView):

    model = Projects
    fields = ["project_name", "project_partner", "project_manager"]
    template_name = "KPITracker/projectUpdate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
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
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context


class ManageProject(LoginRequiredMixin, DetailView):

    model = Projects
    template_name = "KPITracker/manageProject.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self, request):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def add_user_to_project(request, lId, pId):

    # print(lId, "   ",pId)
    project_name = str(Projects.objects.filter(id=pId).values_list("project_name", flat=True))
    project_name = project_name[project_name.find("'")+1:]
    project_name = project_name[:project_name.find("'")]
    # print(project_name)
    UserList.objects.filter(id=lId).update(on_project=project_name)
    user_id = request.user.id
    date = datetime.date.today().strftime("%d-%m-%Y")
    project = UserList.objects.filter(id=user_id).values_list("on_project", flat=True)[0]
    if UserList.objects.filter(id=user_id).values_list("user_type", flat=True)[0] == "Tester":
        if not KPIReport.objects.filter(reporter_id=user_id, report_date=date, on_project=project).exists():
            if project:
                KPIReport.objects.create(reporter_id=UserList.objects.filter(id=user_id).get(), on_project=str(project),
                                         report_date=date)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def rem_user_from_project(request, lId, pId):

    UserList.objects.filter(id=lId).update(on_project="None")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class EditDesc(LoginRequiredMixin, UpdateView):

    model = Projects
    template_name = "KPITracker/manageProjectDesc.html"
    fields = ["description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-project", args=[self.object.id])


class PersonalInfoView(LoginRequiredMixin, DetailView):
    model = UserList
    template_name = "KPITracker/personalInfo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["report"] = apps.get_model("KPITracker", "KPIReport").objects.filter(reporter_id=self.request.user.id,
                                                                                     report_date=datetime.date.today().strftime(
                                                                                         "%d-%m-%Y"))
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["admins"] = list(UserList.objects.filter(user_type="Administrator").values_list("id", flat=True))
        context["admins"] += list(UserList.objects.filter(user_type="Accountant").values_list("id", flat=True))
        return context


class ManageLocations(LoginRequiredMixin, CreateView):
    model = LocationsRegistered
    template_name = "KPITracker/manageLocations.html"
    fields = ["name", "country", "region", "city", "street", "number", "zipcode", "lat", "lon", "misc_description"]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context

    def get_success_url(self):
        return reverse("KPIndustry:manage-locations")

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "KPITracker/passwordReset"
    email_template_name = "KPITracker/passwordResetEmail.html"


class LogIn(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        user_id = self.request.user.id
        date = datetime.date.today().strftime("%d-%m-%Y")
        project = UserList.objects.filter(id=user_id).values_list("on_project", flat=True)[0]
        if UserList.objects.filter(id=user_id).values_list("user_type", flat=True)[0] == "Tester":
            if not KPIReport.objects.filter(reporter_id=user_id, report_date=date, on_project=project).exists():
                if project:
                    KPIReport.objects.create(reporter_id=UserList.objects.filter(id=user_id).get(), on_project=str(project), report_date=date)
        return reverse("KPIndustry:homepage")


class ReportCompleting(LoginRequiredMixin, UpdateView):
    model = KPIReport
    template_name = "KPITracker/dailyReport.html"
    fields = ["critical_issues", "major_issues", "medium_issues", "minor_issues", "test_cases_started", "test_cases_passed", "test_cases_partially_passed",
              "test_cases_failed", "test_cases_blocked"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["report"] = apps.get_model("KPITracker", "KPIReport").objects.filter(reporter_id=self.request.user.id,
                                                                                     report_date=datetime.date.today().strftime(
                                                                                         "%d-%m-%Y"))
        context["work_locations"] = LocationsRegistered.objects.values_list("name", flat=True)
        context["objects"] = self.model.objects.all()
        context["users"] = apps.get_model("KPITracker", "UserList").objects.all()
        context["projects"] = apps.get_model("KPITracker", "Projects").objects.all()
        return context