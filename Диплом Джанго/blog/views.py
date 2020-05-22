from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from blog.templates.blog.models import Partnerorganizations
from blog.templates.blog.models import Project_implementation_plan
from blog.templates.blog.models import Publiczna_presentation
from blog.templates.blog.models import Product_of_innovation
from blog.templates.blog.models import Prognoz_razvitia_nex_year


@login_required(login_url='/admin')
def  post_list(request):
    partnerorganizations = Partnerorganizations.objects.all()
    return render(request, 'blog/post_list.html', {'Организации партнеры': partnerorganizations})
