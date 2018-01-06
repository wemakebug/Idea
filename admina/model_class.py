# -*- encoding:utf-8 -*-
from . import models as admina_models
from django.views.generic.edit import *
from django.views.generic.list import *
from django.views.generic.detail import *
from django.http import *
from django.utils import timezone
''' 基于类的视图 '''
'''Creation'''
class CreatinoDisplayAll(ListView):
    model = admina_models.Creation
    success_url = '/admina/'
    template_name = 'ClassView/CreationDisPlay.html'
    context_object_name = 'Creations'
    ordering = '-Id'
    paginate_by = 20

class CreationDetailView(DetailView):
    model = admina_models.Creation


    def get_context_data(self, **kwargs):
        ctx = super(CreationDetailView,self).get_context_data(**kwargs)
        ctx['now'] = timezone.now()
        return ctx