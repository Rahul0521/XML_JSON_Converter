# converter/forms.py

from django import forms

class XMLFileForm(forms.Form):
    file = forms.FileField()
