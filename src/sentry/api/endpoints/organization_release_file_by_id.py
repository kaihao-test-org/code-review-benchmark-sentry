from sentry.api.bases.organization import OrganizationEndpoint
from sentry.api.exceptions import ResourceDoesNotExist
from sentry.api.helpers.release_file_lookup import lookup_release_file
from sentry.api.serializers import serialize
from sentry.models import ReleaseFile


class OrganizationReleaseFileByIdEndpoint(OrganizationEndpoint):
    def get(self, request, organization, file_id):
        """
        Retrieve a Release File by ID
        `````````````````````````````

        Return metadata for a single release file by its numeric id. This is
        a convenience lookup used by the release artifacts UI when the file's
        release version is not known.

        :pparam string organization_slug: the slug of the organization.
        :pparam string file_id: the numeric id of the release file.
        :auth: required
        """
        try:
            releasefile = lookup_release_file(ReleaseFile.objects, organization.id, file_id)
        except ReleaseFile.DoesNotExist:
            raise ResourceDoesNotExist

        return self.respond(serialize(releasefile, request.user))
