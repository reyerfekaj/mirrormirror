#files.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):

  transcript = forms.CharField(widget=forms.Textarea, label=_("Transcript"))
  transcript = forms.CharField(widget=forms.Textarea, label=_("Transcript"))