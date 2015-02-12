class TestRequiredMixin(object):

    @classmethod
    def pre_dispatch(self, request):
        if not hasattr(request, 'contact'):
            raise Exception('Unauthorized')

        if 'extra' not in request.contact:
            request.contact['extra'] = 'YO'

        if not request.contact.get('extra', False) == 'YO':
            raise Exception('Unauthorized')


class ContactExtraMixin(object):

    @classmethod
    def pre_dispatch(self, request):
        if request.contact.get('extra', None) is None:
            raise Exception("No extra in contact!")
        request.contact['extra'] = 'yo, dude'
