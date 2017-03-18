from django.core.mail import send_mail
from django.conf import settings


def send_success_email (user):
    send_mail('Account Created',
            'Your account was successfully created \n\nYour username is: {username}'
            .format(username=user.username, password=user.password),
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )
