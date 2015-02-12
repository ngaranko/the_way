from django.http import HttpResponse
from django.views.generic import View
from .mixins import TestMixin
from .mixins import TestRequiredMixin


class HomePageView(TestMixin, TestRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        print("I'm HomePageView")
        if not self.contact.get('extra', None) == 'YO':
            raise Exception("MEH!")

        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("Yo, wazzup. {}".format(self.contact))
