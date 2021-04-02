from django.core.mail import send_mail


def send_activation_email(user):
    subject = 'Site registering'
    body = f'Activate code: http://localhost:8000/account/activate/{user.activation_code}/'
    from_email = 'site@django.com'
    recipients = [user.email]
    send_mail(subject=subject, message=body, from_email=from_email, recipient_list=recipients, fail_silently=False)
