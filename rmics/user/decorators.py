from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import redirect, render


def unauthenticated_logic(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func

def allowed_groups(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Error 403: Unauthorized Access")
        return wrapper_func
    return decorator
#TEST COMMIT