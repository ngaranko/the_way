class TestMixin(object):
    def dispatch(self, request, *args, **kwargs):
        print("I'm TestMixin")
        if request.GET.get('logged_in', False):
            self.contact = dict(name='Contact', active=True)
        else:
            raise Exception('123')
        return super(TestMixin, self).dispatch(request, *args, **kwargs)


class TestRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        print("I'm TestRequired")
        self.contact['extra'] = 'YO!'
        return super(TestRequiredMixin, self).dispatch(request, *args, **kwargs)
