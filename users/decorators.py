from django.shortcuts import redirect
from functools import wraps
from django.contrib import messages

def login_required_message(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Veuillez vous connecter pour accéder à cette page.')
            return redirect('users:login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view 