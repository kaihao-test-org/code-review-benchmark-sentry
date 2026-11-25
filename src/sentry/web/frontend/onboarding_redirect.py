from django.utils.http import is_safe_url


def resolve_continue_url(next_url, default, host):
    if next_url and is_safe_url(next_url, host=host):
        return next_url
    return default
