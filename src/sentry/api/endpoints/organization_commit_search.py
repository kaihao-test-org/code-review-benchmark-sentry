from sentry.api.bases.organization import OrganizationEndpoint
from sentry.api.helpers.commit_search import build_author_commit_query
from sentry.api.serializers import serialize
from sentry.models import Commit


class OrganizationCommitSearchEndpoint(OrganizationEndpoint):
    def get(self, request, organization):
        """
        Search an Organization's Commits by Author
        ``````````````````````````````````````````

        Return a list of commits whose author email matches the query.

        :pparam string organization_slug: the slug of the organization.
        :qparam string query: the author email fragment to search for.
        :auth: required
        """
        email_fragment = request.GET.get("query", "")

        sql, params = build_author_commit_query(organization.id, email_fragment)
        results = list(Commit.objects.raw(sql, params))

        return self.respond(serialize(results, request.user))
