from django.conf import settings as django_settings


def settings(request):
    return dict(    # wrapped oddly to stay narrow
        (k, getattr(django_settings, k))
        for k in django_settings.SETTINGS_IN_CONTEXT
    )
