def serialize_app_token(obj, access):
    return {
        "id": obj.id,
        "name": obj.name,
        "webhookUrl": obj.webhook_url,
        "clientId": obj.client_id,
        "clientSecret": obj.client_secret,
    }
