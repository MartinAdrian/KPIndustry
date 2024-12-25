from django.db import models

class UserList(models.Model):
    FirstName = models.CharField("First Name", max_length=100)
    LastName = models.CharField("Last Name", max_length=100)
    eMail = models.CharField("eMail", max_length=100)
    UserType = models.CharField("User Type", max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}:\neMail: {self.eMail}\nType: {self.UserType}"