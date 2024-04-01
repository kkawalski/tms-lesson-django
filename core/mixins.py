from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin

from django.db import models

class OwnOrRedirectMixin:
    user_foreign_key = None

    def dispatch(self: SingleObjectMixin, request: HttpRequest, *args, **kwargs):
        instance: models.Model = self.get_object()
        if getattr(instance, self.user_foreign_key) != request.user:
            detail_url = f'{instance.__class__.__name__.lower()}-detail'
            return HttpResponseRedirect(reverse_lazy(detail_url,  args=[instance.pk]))
        return super().dispatch(request, *args, **kwargs)

