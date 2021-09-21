from django import forms
from django.core.exceptions import ValidationError
from validator.validators import Validators


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Nombre'
                               }
                           ),
                           error_messages={
                               'required': 'Tu nombre es requerido'
                           }
                           )
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder': 'Email'
                                 }
                             ),
                             error_messages={
                                 'required': 'Tu email es requerido'
                             }
                             )
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(
                                  attrs={
                                      'placeholder': 'Asunto'
                                  }
                              ),
                              error_messages={
                                  'required': 'Tu asunto es requerido'
                              }
                              )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Mensaje',
                'rows': 5,
            })

    )

    def clean_email(self):
        email = self.cleaned_data['email']
        validator = Validators(email)
        if validator.validateEmail('El Email no es valido'):
            raise validator.validateEmail('El Email no es valido')
        return email

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        validator = Validators(subject)
        if validator.validateStringLength(f'El asunto {subject} debe ser mas largo',10):
            raise validator.validateStringLength(f'El asunto {subject} debe ser mas largo',10)
        return subject