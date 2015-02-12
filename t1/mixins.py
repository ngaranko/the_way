class TestMixin(object):
    def dispatch(self, request, *args, **kwargs):
        print("I'm test")
        return super(TestMixin, self).dispatch(request, *args, **kwargs)
