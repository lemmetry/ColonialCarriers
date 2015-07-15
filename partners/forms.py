from django import forms
from captcha.fields import ReCaptchaField
from .models import Facility


class PickupForm(forms.Form):
    facility = forms.ModelChoiceField(queryset=Facility.objects.order_by('name'),
                                      label='Location',
                                      empty_label='Select location',
                                      error_messages={'required': 'Location is required.'},
                                      widget=forms.Select(attrs={
                                          'class': 'form-control',
                                          'style': 'max-width: 300px;'}))
    # TODO auto-populate address based on ModelChoiceField selected
    # address = forms.CharField(required=False)
    item_description = forms.CharField(min_length=10,
                                       max_length=250,
                                       label="Item(s) description",
                                       error_messages={'required': 'Description is required.',
                                                       'min_length': 'Provide little more details.'},
                                       widget=forms.Textarea(attrs={
                                           'class': 'form-control',
                                           'rows': 3,
                                           'style': 'max-width: 300px',
                                           'placeholder': 'Please provide information about an item(s). Example: Grey plush elephant.'
                                       }))
    additional_information = forms.CharField(required=False,
                                             max_length=250,
                                             label="Additional information",
                                             widget=forms.Textarea(attrs={
                                                 'class': 'form-control',
                                                 'rows': 3,
                                                 'style': 'max-width: 300px',
                                                 'placeholder': "Please provide additional information to maximaze guest's experience. Example: My daughter's Emely favorite toy."}))
    captcha = ReCaptchaField(label='',
                             error_messages={'required': 'Are you a robot?'})

