from django.shortcuts import render

from django.contrib.auth.models import User

from .models import *

def page(request):

    c = {}

    c['profile'] = Profile.objects.get(user = User.objects.get(username = 'vox.ver'))

    c['posts'] = Post.objects.filter(user = User.objects.get(username = 'vox.ver')).order_by('-created_at')

    return render(request, 'page.html', c)