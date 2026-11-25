MASKED_VALUE = "*" * 64


def serialize_app_token(obj, access):
    if access.has_scope("org:admin"):
        client_secret = obj.client_secret
    else:
        client_secret = MASKED_VALUE
    return {
        "id": obj.id,
        "name": obj.name,
        "webhookUrl": obj.webhook_url,
        "clientId": obj.client_id,
        "clientSecret": client_secret,
    }
