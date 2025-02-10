import datetime
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
    active = models.BooleanField("Ongoing")
    description = models.TextField("Project Description", max_length=2000, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.start_date and not self.end_date:
            self.project_activity = "Not Started"
            super(Projects, self).save(*args, **kwargs)
        elif self.start_date and self.end_date:
            self.project_activity = "Finished"
            self.active = False
            super(Projects, self).save(*args, **kwargs)
        else:
            self.project_activity = "Ongoing"
            self.start_date = datetime.datetime.now()
            super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return (f"Name: {self.project_name}\n"
                f"Project Manager: {self.project_manager}\n"
                f"Ongoing: {"Yes" if self.active == True else "Done/Not Started"}")


class UserList(User):

    user_type = models.CharField("User Type", max_length=100)
    on_project = models.CharField("Assigned Project", max_length=100, default="None")
    gross_salary = models.CharField("Gross Salary", max_length=100, null=True)
    phone_number = models.IntegerField("Phone Number", null=True)
    work_location = models.CharField("Work Location", null=True, max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}:\neMail: {self.email}\nType: {self.user_type}"


class LocationsRegistered(models.Model):
    name = models.CharField("Location Name", null=True, max_length=200)
    lat = models.CharField("Latitude", null=True, max_length=200)
    lon = models.CharField("Longitude", null=True, max_length=200)
    country = models.CharField("Country", null=True, max_length=200)
    region = models.CharField("Region", null=True, max_length=200)
    city = models.CharField("City", null=True, max_length=200)
    street = models.CharField("Street", null=True, max_length=200)
    number = models.CharField("Number", null=True, max_length=200)
    zipcode = models.IntegerField("Number", null=True)

    def __str__(self):
        return f"{self.country}, {self.region}, {self.city}, {self.street}, {self.number}, {self.zipcode}"