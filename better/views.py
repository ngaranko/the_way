from django.http import HttpResponse
from django.views.generic import View
from .mixins import TestMixin
from .mixins import TestRequiredMixin


class BetterView(View):
    def dispatch(self, request, *args, **kwargs):
        meta = getattr(self, 'Meta', None)
        if meta is not None and hasattr(meta, 'pre_dispatchers'):
            for cls in meta.pre_dispatchers:
                response = cls.pre_dispatch(request)
                if response is not None:
                    return response

        if hasattr(self, 'pre_dispatch'):
            response = self.pre_dispatch(request)
            if response is not None:
                return response

        return super(BetterView, self).dispatch(request, *args, **kwargs)


class HomePageView(BetterView):
    class Meta:
        pre_dispatchers = [
            TestMixin,
            TestRequiredMixin,
        ]

    def pre_dispatch(self, request):
        if request.contact.get('extra', None) is None:
            raise Exception("No extra in contact!")

    def get(self, request, *args, **kwargs):
        return HttpResponse("Wazzup?! {}".format(request.contact))
