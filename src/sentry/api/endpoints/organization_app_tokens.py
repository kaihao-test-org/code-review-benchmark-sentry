from sentry.api.bases.organization import OrganizationEndpoint
from sentry.api.serializers.models.app_token import serialize_app_token
from sentry.models import SentryAppInstallation


class OrganizationAppTokensEndpoint(OrganizationEndpoint):
    def get(self, request, organization):
        """
        List an Organization's Installed App Tokens
        ```````````````````````````````````````````

        Return the internal integration installations for the organization.

        :pparam string organization_slug: the slug of the organization.
        :auth: required
        """
        installations = SentryAppInstallation.objects.filter(organization=organization)
        results = [
            serialize_app_token(install.sentry_app.application, request.access)
            for install in installations
        ]
        return self.respond(results)
