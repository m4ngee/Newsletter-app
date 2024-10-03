from typing import Any
from django import forms
from .models import Sub
from .models import Newsletter

class SubFrom(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ['name', 'email']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'body']
    
class NewsletterSendForm(forms.Form):
    newsletter = forms.ModelChoiceField(
        queryset=Newsletter.objects.all(),
        to_field_name='newsletter_id',
        label='Select Newsletter to Send',
        widget=forms.Select
    )


    
    #def clean_email(self):
     #   email = self.cleaned_data.get('email')
      #  if Subscriber.objects.filter(email=email).exists():
       #     raise forms.ValidationError("This email is already subscribed.")
        #return email