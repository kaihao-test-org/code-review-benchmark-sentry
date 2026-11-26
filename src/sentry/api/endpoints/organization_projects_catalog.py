from sentry.api.bases.organization import OrganizationEndpoint, OrganizationPermission
from sentry.models import Project, ProjectStatus


class OrganizationProjectsCatalogEndpoint(OrganizationEndpoint):
    permission_classes = (OrganizationPermission,)

    def get(self, request, organization):
        """
        List an Organization's Project Catalog
        ``````````````````````````````````````

        Return a lightweight catalog of the organization's projects for use
        by the global project switcher.

        :pparam string organization_slug: the slug of the organization.
        :auth: required
        """
        projects = Project.objects.filter(
            organization=organization, status=ProjectStatus.VISIBLE
        ).order_by("slug")

        return self.respond(
            [{"id": p.id, "slug": p.slug, "name": p.name, "platform": p.platform} for p in projects]
        )
