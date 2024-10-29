from django import forms
from mailing.models import Client, Mailing, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["email", "full_name"]


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['description', 'periodicity', 'status', 'message', 'client']
