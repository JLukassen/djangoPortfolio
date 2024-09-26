from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'job_description']
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4}),
        }
