import ipaddress
import socket
from urllib.parse import urlparse

import requests


def _is_public_address(host):
    for info in socket.getaddrinfo(host, None):
        ip = ipaddress.ip_address(info[4][0])
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
            or ip.is_unspecified
        ):
            return False
    return True


def fetch_webhook_preview(url):
    host = urlparse(url).hostname
    if not host or not _is_public_address(host):
        raise ValueError("refusing to connect to a non-public address")

    response = requests.get(url, timeout=5, allow_redirects=False)
    return {
        "status": response.status_code,
        "headers": dict(response.headers),
        "body": response.text[:2048],
    }
