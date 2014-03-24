from django.core.urlresolvers import resolve
from django.shortcuts import redirect


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def super_redirect(request, url_name):
    '''
    A terrible name for just being able to redirect without hard-coding the
    current namespace.
    '''
    resolver = resolve(request.path)
    fully_qualified_url_name = url_name

    if resolver.app_name:
        fully_qualified_url_name = '%s:%s' % (resolver.app_name, fully_qualified_url_name)

    if resolver.namespace:
        fully_qualified_url_name = '%s:%s' % (resolver.namespace, fully_qualified_url_name)

    return redirect(fully_qualified_url_name)
