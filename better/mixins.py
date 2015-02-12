class TestMixin(object):

    @classmethod
    def pre_dispatch(cls, request):
        if not hasattr(request, 'contact'):
            request.contact = dict(name='Contact', active=True)

        if not request.contact.get('active', False):
            raise Exception('Unauthorized')


class TestRequiredMixin(object):

    @classmethod
    def pre_dispatch(self, request):
        if not hasattr(request, 'contact'):
            raise Exception('Unauthorized')

        if 'extra' not in request.contact:
            request.contact['extra'] = 'YO'

        if not request.contact.get('extra', False) == 'YO':
            raise Exception('Unauthorized')

