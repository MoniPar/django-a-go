from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """
    Updates Django's User Model
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Updates the Profile Model
    """
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '(+xxx)xxx-xxxxxxx'}))
    occasion_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'yyyy-mm-dd'}))
    occasion_type = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'E.g. Wedding'}))
    occasion_requirement = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'E.g. Bridal Gown, 1x Mother of the Bride etc'}))

    class Meta:
        model = Profile
        fields = [
            'phone', 'occasion_date', 'occasion_type', 'occasion_requirement'
        ]
