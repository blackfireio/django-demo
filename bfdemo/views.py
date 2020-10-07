# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import random
import time
from django.http import HttpResponse
from .models import Comment
from django.template import loader
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.core.signals import request_finished


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
    v = weighted_random(
        {
            2: 5,
            1.5: 10,
            0.9: 20,
            0.6: 25,
            0.3: 10,
            0.1: 20,
            0.05: 10
        }
    )
    time.sleep(v)

    err = weighted_random({True: 5, False: 95})
    if err:
        raise Exception('')

    spike_mem = weighted_random({True: 15, False: 85})
    if spike_mem:
        d = ['A'] * 100000000

    response = 'Hi there!'
    spike_output = weighted_random({True: 20, False: 80})
    if spike_output:
        response = 'a' * 200 * 1024  # 200 Kb

    return HttpResponse(response)


def apm_autoprofile(request):
    return HttpResponse("autoprofile page")


def _my_req_finished_callback(sender, **kwargs):
    print('_my_req_finished_callback callled!')


class AllInOneView(View):

    def get(self, request):

        # generate user if not exists
        try:
            user = User.objects.get(username='sumer')
        except User.DoesNotExist:
            user = None

        if user is None:
            user = User.objects.create_user(
                'sumer', 'sumer@cip.com', 'password'
            )
            user.save()

        # auth
        user = authenticate(
            request=request, username='sumer', password='password'
        )
        login(request, user)

        if request.user.is_authenticated:
            print("User is authenticated")

        # session
        request.session['test'] = 1
        _ = request.session['test']
        _ = request.session.get('not_existent_key', None)
        request.session.delete('test')

        # cache
        cache.set('k', 1)
        v = cache.get('k')
        cache.incr('k')
        cache.decr('k')

        # signals
        request_finished.connect(_my_req_finished_callback)

        # load template
        template = loader.get_template('allinone.html')
        context = {}

        return HttpResponse(template.render(context, request))


def nplusone(request):
    #_ = requests.get('https://blackfire.io/')
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
