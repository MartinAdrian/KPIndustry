import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models


class Projects(models.Model):

    project_name = models.CharField("Project Name", max_length=100)
    project_partner = models.CharField("Project Partner", max_length=100, null=True)
    project_manager = models.CharField("Project Manager", max_length=100)
    project_activity = models.CharField("Project Activity", max_length=100, null=True)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    reopened=models.BooleanField(default=False)
    active = models.BooleanField("Ongoing")

    def save(self, *args, **kwargs):
        if self.project_activity is None and self.active == False:
            self.active = False
            self.project_activity = "Not Started"
            super(Projects, self).save(*args, **kwargs)
        elif self.project_activity == "Ongoing" and self.active == False:
            self.project_activity = "Finished"
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
    on_project = models.CharField("Assigned Project", max_length=100, null=True)

    def save(self, *args, **kwargs):
        if not "sha" in self.password:
            self.password = make_password(self.password)
            super(UserList, self).save(*args, **kwargs)
        else:
            super(UserList, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}:\neMail: {self.email}\nType: {self.user_type}"