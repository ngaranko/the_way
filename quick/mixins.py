class TestMixin(object):
    _contact = None

    @property
    def contact(self):
        if self._contact is None:
            self._contact = dict(name='Contact', active=True)
        return self._contact

    def dispatch(self, request, *args, **kwargs):
        if not self.contact.get('active', False):
            raise Exception('Unauthorized')

        return super(TestMixin, self).dispatch(request, *args, **kwargs)


class TestRequiredMixin(object):
    @property
    def contact(self):
        original = super(TestRequiredMixin, self).contact
        original['extra'] = 'YO'
        return original

    def dispatch(self, request, *args, **kwargs):
        if not self.contact.get('extra', False) == 'YO':
            raise Exception('Unauthorized')
        return super(TestRequiredMixin, self).dispatch(request, *args, **kwargs)
