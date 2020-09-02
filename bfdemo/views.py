# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import random
import time
from django.http import HttpResponse
from .models import Comment
from django.template import loader


#comments = request.user.user_comments.all()
def weighted_random(weight_dict):
    """weight_dict : { value1:weight1 , ...}
    Tested with below:
    import utils
    from collections import Counter
    c = Counter()
    for _ in range(20000):
        c[utils.weighted_random({1:50,2:50,3:1})] += 1
    >>Counter({2: 9911, 1: 9862, 3: 227})
    """
    rnd = random.random() * sum(weight_dict.values())
    for val, w in weight_dict.items():
        rnd -= w
        if rnd < 0:
            return val


def load_me(request):
    v = weighted_random({2: 5, 1.5: 10, 0.9: 20, 0.6: 25, 0.3: 10, 0.1: 30})
    time.sleep(v)

    err = weighted_random({True: 5, False: 95})
    if err:
        raise Exception('')

    spike_mem = weighted_random({True: 15, False: 85})
    if spike_mem:
        d = ['A'] * 100_000_000

    response = 'Hi there!'
    spike_output = weighted_random({True: 20, False: 80})
    if spike_output:
        response = 'a' * 200 * 1024  # 200 Kb

    return HttpResponse(response)


def nplusone(request):
    _ = requests.get('https://blackfire.io/')
    comments = Comment.objects.all()
    template = loader.get_template('nplusone.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def nplusone_fix(request):
    comments = Comment.objects.select_related('user').all()
    template = loader.get_template('nplusone-fix.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def memspike(request):
    comments = Comment.objects.all()
    template = loader.get_template('memspike.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))


def memspike_fix(request):
    comments = Comment.objects.all().iterator()
    template = loader.get_template('memspike-fix.html')
    context = {'comments': comments}
    return HttpResponse(template.render(context, request))
