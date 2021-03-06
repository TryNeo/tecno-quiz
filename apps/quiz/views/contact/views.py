from apps.quiz.forms import ContactForm
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.core.mail import EmailMessage

from TecnoQuiz.settings.production import EMAIL_HOST_USER,GOOGLE_RECAPTCHA_SECRET_KEY

import threading
import os
import json
import urllib

def send_email(name, email, subject, message):
    template_email = render_to_string('Contact/template_email.html',
            {
                'name': name,
                'email': email,
                'message': message
            }
        )
    send_email = EmailMessage(
        subject,
        template_email,
        EMAIL_HOST_USER,
        ['ts.josu3@gmail.com']
    )
    send_email.fail_silently = False
    send_email.send()


class ContactView(FormView):
    template_name = 'Contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('quiz:contact')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.get_form()
                if form.is_valid():
                    recaptcha_response = request.POST.get('g-recaptcha-response')
                    url = 'https://www.google.com/recaptcha/api/siteverify'
                    values = {
                        'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recaptcha_response,
                        }
                    data = urllib.parse.urlencode(values).encode()
                    req =  urllib.request.Request(url, data=data)
                    response = urllib.request.urlopen(req)
                    result = json.loads(response.read().decode())

                    name = request.POST['name']
                    email = request.POST['email']
                    subject = request.POST['subject']
                    message = request.POST['message']
                    thread = threading.Thread(target=send_email, kwargs={
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message
                    })
                    if result['success']:
                        thread.start()
                        data = {'status': 1, 'message': 'Mensaje enviado correctamente'}
                    else:
                        data = {'status': 0, 'message': {'reCAPTCHA':'reCaPTCHA invalidado , completa el reCAPTCHA'}}
                else:
                    data = {'status': 0, 'message': form.errors}
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
