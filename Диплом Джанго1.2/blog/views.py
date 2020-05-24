from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request

from blog.apps import home_work
from blog.models import Homework


@login_required(login_url='/admin')
def post_list(request):
    Homework.objects.filter(avtor=request.user)
    return render(request, 'blog/post_list.html', {'home_work': home_work})



