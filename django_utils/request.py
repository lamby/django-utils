from django.core.urlresolvers import resolve
from django.shortcuts import redirect

IP_LENGTH = 4
MAX_IP_VAL = 255


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


def convert_ip_to_number(ip):
    str_ip = ''.join([a.zfill(3) for a in ip.split('.')])
    return int(str_ip)


def is_ip_in_range(ip, start, end):
    ip_num = convert_ip_to_number(ip)
    start_num = convert_ip_to_number(start)
    end_num = convert_ip_to_number(end)
    return start_num <= ip_num <= end_num


def is_ip_in_list(ip, ip_list):
    for ip_range in ip_list:
        if isinstance(ip_range, (tuple, list)) and len(ip_range) >= 2:
            # start/end
            start = ip_range[0]
            end = ip_range[1]
            ret = is_ip_in_range(ip, start, end)
        else:
            # single address
            if isinstance(ip_range, (tuple, list)):
                ip_range = ip_range[0]
            ret = ip.strip() == ip_range.strip()

        if ret:
            return True
    return False


def is_internal(request):
    ip = get_client_ip(request)
    internal_ips = [
        ('208.75.169.0', '208.75.169.255'),     # Duke Street
        ('62.189.234.210', '62.189.234.214'),   # UK
        ('10.0.0.1', '10.255.255.255'),         # Private Class A Network
        '127.0.0.1'     # localhost
    ]
    return is_ip_in_list(ip, internal_ips)
