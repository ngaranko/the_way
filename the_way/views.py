from django.http import HttpResponse
from django.views.generic import View
from .mixins import TestRequiredMixin
from .mixins import ContactExtraMixin


class HomePageView(View):
    class Meta:
        pre_dispatchers = [
            TestRequiredMixin,
            ContactExtraMixin,
        ]

    def get(self, request, *args, **kwargs):
        return HttpResponse("Wazzup?! {}".format(request.contact))
