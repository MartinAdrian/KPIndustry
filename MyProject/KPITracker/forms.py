from django.forms import ModelForm
from django import forms
from KPITracker.models import UserList
import requests
from bs4 import BeautifulSoup


class AddUserForm(ModelForm):

    country_code = forms.CharField()
    country_code_list = forms.ModelChoiceField(queryset=codes)

    class Meta:
        model = UserList
        fields = ["first_name", "last_name", "email", "username", "user_type", "gross_salary", "phone_number", "work_location"]

    def clean(self):
        data = self.cleaned_data
        if not data.fields["phone_number"].isdigit and len(data.fields["phone_number"]) == 9:
            message = "Phone number is not valid"
            self._errors["phone_number"] = self.error_class([message])
        data.fields["phone_number"] = data.fields["country_code"] + data.fields["phone_number"]
        return data
