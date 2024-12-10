from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"


# class SimpleForm(forms.Form):
#     subject=forms.CharField(max_length=150)
#     message = forms.Textarea()