from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_logic(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func

#WRITE DECORATOR HERE FOR USER TYPE REQUIRED FOR A SPECIFIC VIEW