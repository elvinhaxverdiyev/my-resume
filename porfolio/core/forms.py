from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
