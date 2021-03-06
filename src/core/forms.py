"""
Forms for general CSHC app use
"""
from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from zinnia.models import Entry, Category
from zinnia.admin.forms import EntryAdminForm, CategoryAdminForm
from unify.widgets import UnifyTextInput, UnifyPhoneInput, UnifyTextarea, UnifySelect, UnifyCheckboxInput
from .models import JuniorsContactSubmission, ContactSubmission, CshcUser


class UserProfileForm(forms.ModelForm):
    """ Form used by a user editing their own details. """

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = CshcUser
        fields = ('email', 'first_name', 'last_name')
        widgets = {
            'first_name': UnifyTextInput(left_icon='fas fa-user'),
            'last_name': UnifyTextInput(left_icon='fas fa-user'),
            'email': forms.HiddenInput(),
        }


class SignupFormExtra(forms.Form):
    """ Custom form for additional sign-up information """
    first_name = forms.CharField(max_length=30,
                                 label='First name',
                                 widget=UnifyTextInput(
                                     attrs={
                                         'placeholder': 'First name',
                                         'class': 'g-py-15 g-pr-15',
                                     },
                                     left_icon='fas fa-user'))
    last_name = forms.CharField(max_length=30,
                                label='Last name',
                                widget=UnifyTextInput(
                                    attrs={
                                        'placeholder': 'Last name',
                                        'class': 'g-py-15 g-pr-15',
                                    },
                                    left_icon='fas fa-user'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = UnifyTextInput(
            attrs={
                'placeholder': 'E-mail address',
                'class': 'g-py-15 g-pr-15',
            },
            left_icon='fas fa-envelope')

    def signup(self, request, user):
        """
        Required method that is called by the django-allauth's form when saving
        a new user.
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class ContactSubmissionForm(forms.ModelForm):
    """ Form used for the contact form"""
    captcha = ReCaptchaField()

    class Meta:
        """ Meta-info for the form. """
        model = ContactSubmission
        # our_notes is only to be used by staff/admin
        exclude = ('our_notes',)
        help_texts = {
            'message': None,
        }
        widgets = {
            'first_name': UnifyTextInput(attrs={'placeholder': 'First Name*'}, left_icon='fas fa-user'),
            'last_name': UnifyTextInput(attrs={'placeholder': 'Last Name*'}, left_icon='fas fa-user'),
            'email': UnifyTextInput(attrs={'placeholder': 'E-mail Address*'}, left_icon='fas fa-envelope'),
            'phone': UnifyPhoneInput(attrs={'placeholder': 'Phone'}),
            'message': UnifyTextarea(attrs={'placeholder': 'Message*', 'rows': '5'}),
            'mailing_list': UnifyCheckboxInput(label='I would like to join the Club mailing list'),
        }


class JuniorsContactSubmissionForm(forms.ModelForm):
    """ Form used for the contact form"""
    captcha = ReCaptchaField()

    class Meta:
        """ Meta-info for the form. """
        model = JuniorsContactSubmission
        # our_notes is only to be used by staff/admin
        exclude = ('our_notes',)
        help_texts = {
            'message': None,
        }
        labels = {
            'trigger': 'How did you hear about Cambridge South Junior Hockey?',
        }
        widgets = {
            'first_name': UnifyTextInput(attrs={'placeholder': 'First Name*'}, left_icon='fas fa-user'),
            'last_name': UnifyTextInput(attrs={'placeholder': 'Last Name*'}, left_icon='fas fa-user'),
            'email': UnifyTextInput(attrs={'placeholder': 'E-mail Address*'}, left_icon='fas fa-envelope'),
            'phone': UnifyPhoneInput(attrs={'placeholder': 'Phone'}),
            'child_name': UnifyTextInput(attrs={'placeholder': 'Name*'}, left_icon='fas fa-user'),
            'child_gender': UnifySelect,
            'child_age': UnifySelect,
            'message': UnifyTextarea(attrs={'placeholder': 'Message*', 'rows': '5'}),
            'mailing_list': UnifyCheckboxInput(label='I would like to join the Club mailing list'),
            'trigger': UnifySelect,
        }


class FlatPageAdminForm(forms.ModelForm):
    """ Form for editing matches in the admin interface """
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FlatPage
        exclude = []


class ZinniaEntryAdminForm(EntryAdminForm):
    """ Overrides the default admin form, adding a couple of redactor
        editor widget.
    """
    content = forms.CharField(widget=CKEditorUploadingWidget())
    excerpt = forms.CharField(widget=CKEditorUploadingWidget())
    lead = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        """ Meta-info for the form. """
        model = Entry
        exclude = []


class ZinniaCategoryAdminForm(CategoryAdminForm):
    """ Overrides the default admin form, adding a redactor editor widget. """
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        """ Meta-info for the form. """
        model = Category
        exclude = []
