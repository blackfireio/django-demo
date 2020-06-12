# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Comment
from django.template import loader
import requests

#comments = request.user.user_comments.all()


def dummy(request):
    return HttpResponse('Hi!')


def nplusone(request):

    # make a dummy HTTP call
    _ = requests.get('http://127.0.0.1:8000/dummy')

    comments = Comment.objects.all()
    #comments = Comment.objects.select_related('user').all()
    template = loader.get_template('nplusone.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def memspike(request):
    comments = Comment.objects.all()
    #comments = Comment.objects.all().iterator()
    template = loader.get_template('memspike.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))
