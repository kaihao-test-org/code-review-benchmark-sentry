from rest_framework.response import Response

from sentry.api.bases.project import ProjectEndpoint, ProjectSettingPermission
from sentry.api.exceptions import ResourceDoesNotExist
from sentry.api.helpers.key_rotation import log_key_rotation
from sentry.api.serializers import serialize
from sentry.models import ProjectKey, ProjectKeyStatus


class ProjectKeyRotateEndpoint(ProjectEndpoint):
    permission_classes = (ProjectSettingPermission,)

    def post(self, request, project, key_id):
        """
        Rotate a Client Key's Secret
        ````````````````````````````

        Generate a new secret for the given client key.

        :pparam string organization_slug: the slug of the organization.
        :pparam string project_slug: the slug of the project.
        :pparam string key_id: the public key of the client key to rotate.
        :auth: required
        """
        try:
            key = ProjectKey.objects.get(
                project=project, public_key=key_id, roles=ProjectKey.roles.store
            )
        except ProjectKey.DoesNotExist:
            raise ResourceDoesNotExist

        key.secret_key = ProjectKey.generate_api_key()
        key.status = ProjectKeyStatus.ACTIVE
        key.save()

        log_key_rotation(project, key)

        return Response(serialize(key, request.user), status=200)
