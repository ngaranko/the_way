class TestMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.contact = dict(name='Contact', active=True)

        if not self.contact.get('active', False):
            raise Exception('Unauthorized')

        return super(TestMixin, self).dispatch(request, *args, **kwargs)


class TestRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.contact['extra'] = 'YO!'

        if not self.contact.get('extra', False) == 'YO':
            raise Exception('Unauthorized')
        return super(TestRequiredMixin, self).dispatch(request, *args, **kwargs)
