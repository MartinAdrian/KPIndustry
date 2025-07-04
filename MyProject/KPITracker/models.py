import datetime
import json
import string
import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models import CharField
from django.template.loader import render_to_string
from django.views.generic.base import ContextMixin


class Projects(models.Model):

    project_name = models.CharField("Project Name", max_length=100)
    project_partner = models.CharField("Project Partner", max_length=100, null=True)
    project_manager = models.CharField("Project Manager", max_length=100)
    project_activity = models.CharField("Project Activity", max_length=100, null=True)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    active = models.BooleanField("Ongoing", default=True)
    description = models.TextField("Project Description", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.active and not self.start_date:
            self.project_activity = "Not Started"
            super(Projects, self).save(*args, **kwargs)
        elif self.active and not self.start_date:
            self.start_date = datetime.datetime.now()
            self.project_activity = "Ongoing"
            super(Projects, self).save(*args, **kwargs)
        else:
            super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return (f"Name: {self.project_name}\n"
                f"Project Manager: {self.project_manager}\n"
                f"Ongoing: {"Yes" if self.active == True else "Done/Not Started"}")


class UserList(User):

    user_type = models.CharField("User Type", max_length=100)
    on_project = models.CharField("Assigned Project", max_length=100, default="None")
    gross_salary = models.CharField("Gross Salary", max_length=100, null=True)
    phone_number = models.CharField("Phone Number", null=True, max_length=20)
    work_location = models.CharField("Work Location", null=True, max_length=200)

    def save(self):
        if "sha256" not in self.password:
            self.set_password(self.password)
        super().save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}:\neMail: {self.email}\nType: {self.user_type}"


class LocationsRegistered(models.Model):
    name = models.CharField("Location Name", max_length=200, unique=True)
    lat = models.CharField("Latitude", max_length=200)
    lon = models.CharField("Longitude", max_length=200)
    country = models.CharField("Country", max_length=200)
    region = models.CharField("Region", max_length=200)
    city = models.CharField("City", max_length=200)
    street = models.CharField("Street", max_length=200)
    number = models.CharField("Number", max_length=200)
    zipcode = models.IntegerField("Zip Code")
    misc_description = models.TextField("Misc Description",null=True, blank=True)


class KPIReport(models.Model):
    reporter_id = models.ForeignKey(UserList, on_delete=models.RESTRICT)
    report_date = models.CharField("Creation Date", max_length=20)
    on_project = models.CharField("Active Project", max_length=200)
    critical_issues = models.IntegerField("Critical Issues", default=0)
    major_issues = models.IntegerField("Major Issues", default=0)
    medium_issues = models.IntegerField("Medium Issues", default=0)
    minor_issues = models.IntegerField("Minor Issues", default=0)
    optional_issues = models.IntegerField("Optional Issues", default=0)
    test_cases_started = models.IntegerField("Started Test Cases", default=0)
    test_cases_passed = models.IntegerField("Passed Test Cases", default=0)
    test_cases_partially_passed = models.IntegerField("Partially Passed Test Cases", default=0)
    test_cases_failed = models.IntegerField("Failed Test Cases", default=0)
    test_cases_blocked = models.IntegerField("Unable to Check Test Cases", default=0)
    report_observations = models.TextField("Observations", blank=True, null=True, max_length=2000)
    task = models.CharField("Allocated Task", null=True,max_length=200)


class ProjectTasks(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.RESTRICT)
    task_name = models.CharField("Task Name", max_length=200)
    assigned_testers = models.TextField("Assigned testers", blank=True)

    def get_assigned_testers(self):
        return json.loads(self.assigned_testers)

    def set_assigned_testers(self, to_add):
        self.assigned_testers = json.dumps(to_add)