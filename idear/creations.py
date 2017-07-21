# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from admina.models import Creation

from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

# Create your views here.


def creations(req):
	'''
    创意灵感一级二级页面项目显示

	'''
    if req.method == 'GET':
    	sign = req.GET['sign']
        if sign != "":
	        Creation2ProjectLabelObj = Creation2ProjectLabel.objects.get( projectLabel = sign)
	        creations = Creation2ProjectLabelObj.Creation2ProjectLabel_Creation_set.all()
	    else:
            creations = Creation.objects.all()
            projectLabels = ProjectLabel.objects.all()
        return render_to_response('creations/index.html',{'creations':creations,'projectLabels':projectLabels})
    else:
    	id = req.POST['creationId']
    	creation = Creation.objects.fitler(id = id)
    	return render_to_response('creations/sec_creations.html',{'creation':creation,})

