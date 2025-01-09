from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models


class UserList(User):

    user_type = models.CharField("User Type", max_length=100)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserList, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}:\neMail: {self.email}\nType: {self.UserType}"


class Projects(models.Model):

    ProjectName = models.CharField("Project Name", max_length=100)
    ProjectManager = models.CharField("Project Manager", max_length=100)
    ProjectLTs = models.JSONField()
    ProjectTesters = models.JSONField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return (f"Name: {self.ProjectName}\n"
                f"Project Manager: {self.ProjectManager}\n"
                f"Lead Testers: {self.ProjectLTs}\n"
                f"Testers: {self.ProjectTesters}")


