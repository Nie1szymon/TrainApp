from django.conf import settings
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.http import JsonResponse


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )
