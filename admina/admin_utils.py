from functools import wraps
from . import models
from django.shortcuts import render

def check_login():
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            try:
                admin_uuid = request.session.get("admin_uuid")
                admin_user = models.Admin.objects.get(Uuid=admin_uuid)
            except Exception as e:
                print(e)
                return render(request, 'admina/login.html')
            else:
                return func(request, *args, **kwargs)
        return inner
    return decorator