# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Comment
from django.template import loader

#comments = request.user.user_comments.all()


def nplusone(request):
    comments = Comment.objects.all()
    template = loader.get_template('nplusone.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def nplusone_fix(request):
    comments = Comment.objects.select_related('user').all()
    template = loader.get_template('nplusone.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def memspike(request):
    comments = Comment.objects.all()
    template = loader.get_template('memspike.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def memspike_fix(request):
    comments = Comment.objects.all().iterator()
    template = loader.get_template('memspike.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))
