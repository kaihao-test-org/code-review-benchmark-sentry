from rest_framework.response import Response

from sentry.api.bases.organization import OrganizationPermission
from sentry.api.bases.organizationmember import OrganizationMemberEndpoint
from sentry.api.serializers import serialize
from sentry.api.serializers.rest_framework.member_profile import MemberProfileSerializer


class MemberProfilePermission(OrganizationPermission):
    scope_map = {
        "GET": ["org:read", "org:write", "org:admin"],
        "PUT": ["org:read", "org:write", "org:admin"],
    }


class OrganizationMemberProfileEndpoint(OrganizationMemberEndpoint):
    permission_classes = (MemberProfilePermission,)

    def put(self, request, organization, member):
        """
        Update a Member's Profile Preferences
        `````````````````````````````````````

        Update the calling member's own notification and display preferences.

        :pparam string organization_slug: the slug of the organization.
        :pparam string member_id: the member id, or "me".
        :auth: required
        """
        serializer = MemberProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        result = serializer.validated_data

        updates = {}
        if "role" in result:
            updates["role"] = result["role"]
        if updates:
            member.update(**updates)

        return Response(serialize(member, request.user))
