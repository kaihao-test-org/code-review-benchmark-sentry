from rest_framework import serializers
from rest_framework.response import Response

from sentry.api.bases.project import ProjectEndpoint, ProjectSettingPermission
from sentry.api.helpers.webhook_preview import fetch_webhook_preview


class WebhookPreviewSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class ProjectWebhookPreviewEndpoint(ProjectEndpoint):
    permission_classes = (ProjectSettingPermission,)

    def post(self, request, project):
        """
        Preview an Outgoing Webhook
        ```````````````````````````

        Send a request to the configured webhook URL and return the response
        so the user can verify connectivity before saving the integration.

        :pparam string organization_slug: the slug of the organization.
        :pparam string project_slug: the slug of the project.
        :param string url: the webhook URL to test.
        :auth: required
        """
        serializer = WebhookPreviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        url = serializer.validated_data["url"]
        try:
            result = fetch_webhook_preview(url)
        except Exception as exc:
            return Response({"error": str(exc)}, status=400)

        return Response(result)
