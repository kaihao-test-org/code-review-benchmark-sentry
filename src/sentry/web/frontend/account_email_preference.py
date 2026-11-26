from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


@method_decorator(csrf_exempt, name="dispatch")
class AccountEmailPreferenceView(View):
    def post(self, request):
        from sentry.models import UserOption

        if not request.user.is_authenticated():
            return HttpResponse(status=401)

        subscribed = request.POST.get("subscribed") == "1"
        UserOption.objects.set_value(
            user=request.user, key="mail:email_notifications", value=subscribed
        )
        return HttpResponseRedirect("/account/settings/notifications/")
