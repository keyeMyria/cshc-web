"""
Forms for general CSHC app use
"""
from django import forms
from .models import JuniorsContactSubmission


class SignupForm(forms.Form):
    """ Custom form for additional sign-up information """
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')

    def signup(self, request, user):
        """ 
        Required method that is called by the django-allauth's form when saving
        a new user.
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class JuniorsContactSubmissionForm(forms.ModelForm):
    """ Form used for the contact form"""

    class Meta:
        """ Meta-info for the form. """
        model = JuniorsContactSubmission
        # our_notes is only to be used by staff/admin
        exclude = ('our_notes',)
