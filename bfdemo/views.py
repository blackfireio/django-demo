# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Comment
from django.template import loader

def comments(request):
    comments = Comment.objects.all()
    #comments = request.user.user_comments.all()
    #comments = request.user.user_comments.select_related('question').all()
    template = loader.get_template('comments.html')
    context = {
        'comments': comments
    }
    r = HttpResponse(template.render(context, request))
    return r

