from django import forms
from .models import Volunteer, Mentor, ContactPage, MailList, Help_choices
from .countries import COUNTRIES

class VolunteerForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(),label="First Name")
    lastname = forms.CharField(widget=forms.TextInput(),label="Last Name")
    email = forms.EmailField(widget=forms.EmailInput())
    country = forms.Select()
    what_can_you_help_with = forms.ModelMultipleChoiceField(queryset=Help_choices.objects.all(), widget=forms.CheckboxSelectMultiple)
    any_other_area_you_would_like_to_help = forms.CharField(widget=forms.TextInput())
    why_would_you_like_to_help = forms.CharField(widget=forms.Textarea(attrs={'rows' : "5"}))

    class Meta:
        model = Volunteer
        fields = '__all__'

class MentorForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(), label="First Name")
    lastname = forms.CharField(widget=forms.TextInput(), label="Last Name")
    email = forms.EmailField(widget=forms.EmailInput())
    phone_number = forms.CharField(widget=forms.TextInput(), label="Phone Number", required=False)
    company = forms.CharField(widget=forms.TextInput())
    country = forms.Select()
    area_of_interest = forms.CharField(widget=forms.TextInput())
    any_other_details = forms.CharField(widget=forms.Textarea(attrs={'rows' : "5"}))

    class Meta:
        model = Mentor
        fields = '__all__'

class ContactPageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea(attrs={'rows' : "5"}))

    class Meta:
        model = ContactPage
        fields = '__all__'

class MailListForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = MailList
        fields = '__all__'

