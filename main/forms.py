from django import forms
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm as DjangoCreationForm, UsernameField
from . import models
import logging

logger = logging.getLogger(__name__)


# user registration form

class UserCreationForm(DjangoCreationForm):
    class Meta(DjangoCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {'email': UsernameField}

    def send_mail(self):
        logger.info(
            "Sending  signup for  email=%s",
            self.cleaned_data['email'],
        )
        message = "welcome {}".format(self.cleaned_data['email'])
        send_mail(
            "Welcome to JASSTORES",
            message,
            "site@jasstore.domain"
            [self.cleaned_data['email']],
            fail_silently=True
        )


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(max_length=500, widget=forms.Textarea)

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = 'From: {0}\n{1} '.format(
            self.cleaned_data["name"],
            self.cleaned_data["message"]
        )

        send_mail(
            'Site message',
            message,
            'jane@ndirangusDomain',
            ['janendirangu49@gmail.com'],
            fail_silently=False

        )
