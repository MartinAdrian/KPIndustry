from django.db import models

class UserList(models.Model):

    FirstName = models.CharField("First Name", max_length=100)
    LastName = models.CharField("Last Name", max_length=100)
    eMail = models.CharField("eMail", max_length=100)
    Username = models.CharField("Username", max_length=100)
    Password = models.CharField("Password", max_length=100, default="admin")
    UserType = models.CharField("User Type", max_length=100)
    SuperUser = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    DateJoined = models.TimeField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}:\neMail: {self.eMail}\nType: {self.UserType}"


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


