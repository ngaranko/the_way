from django.http import HttpResponse
from django.views.generic import View
from .mixins import TestMixin
from .mixins import TestRequiredMixin


class HomePageView(TestRequiredMixin, TestMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if self.contact.get('extra', None) is None:
            raise Exception("No extra in contact!")

        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("Wazzup?! {}".format(self.contact))
