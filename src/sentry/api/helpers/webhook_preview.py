import requests


def fetch_webhook_preview(url):
    response = requests.get(url, timeout=5, allow_redirects=True)
    return {
        "status": response.status_code,
        "headers": dict(response.headers),
        "body": response.text[:2048],
    }
