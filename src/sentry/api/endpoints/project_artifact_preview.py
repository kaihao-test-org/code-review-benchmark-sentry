import os

from django.conf import settings
from django.http import HttpResponse

from sentry.api.bases.project import ProjectEndpoint, ProjectReleasePermission
from sentry.api.exceptions import ResourceDoesNotExist
from sentry.api.helpers.artifact_cache import resolve_cached_artifact


class ProjectArtifactPreviewEndpoint(ProjectEndpoint):
    permission_classes = (ProjectReleasePermission,)

    def get(self, request, project):
        """
        Preview a Cached Release Artifact
        `````````````````````````````````

        Return the raw contents of a previously extracted release artifact
        from the project's local artifact cache.

        :pparam string organization_slug: the slug of the organization.
        :pparam string project_slug: the slug of the project.
        :qparam string name: the artifact file name to preview.
        :auth: required
        """
        name = request.GET.get("name")
        if not name:
            return HttpResponse(status=400)

        base_dir = os.path.join(settings.MEDIA_ROOT, "artifact-cache", str(project.id))
        path = resolve_cached_artifact(base_dir, name)

        try:
            with open(path, "rb") as fp:
                contents = fp.read()
        except (IOError, OSError):
            raise ResourceDoesNotExist

        return HttpResponse(contents, content_type="application/octet-stream")
