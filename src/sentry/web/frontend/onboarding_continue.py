from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View

from sentry.web.frontend.onboarding_redirect import resolve_continue_url


class OnboardingContinueView(View):
    def get(self, request):
        default = reverse("sentry")
        target = resolve_continue_url(request.GET.get("next"), default)
        return HttpResponseRedirect(target)
