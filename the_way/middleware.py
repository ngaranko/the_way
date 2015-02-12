from django.conf import settings
from django.views.generic.base import View


def get_class(func):
    if not getattr(func, 'func_closure', None):
        return

    for closure in func.func_closure:
        contents = closure.cell_contents

        if not contents:
            continue

        if getattr(contents, '__bases__', None) and issubclass(contents, View):
            return contents

        result = get_class(contents)
        if result:
            return result


class ContactMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        module_name = view_func.__module__.split('.')[0]
        if module_name not in settings.CONTACT_MIDDLEWARE_MODULES:
            return None

        if not hasattr(request, 'contact'):
            request.contact = dict(name='Contact', active=True)

        if not request.contact.get('active', False):
            raise Exception('Unauthorized')


class ViewWithExtrasMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        view_class = get_class(view_func)
        meta = getattr(view_class, 'Meta', None)
        if meta is not None and hasattr(meta, 'pre_dispatchers'):
            for cls in meta.pre_dispatchers:
                response = cls.pre_dispatch(request)
                if response is not None:
                    return response
