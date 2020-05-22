# Create your views here.
from blog.templates.blog.models import Homework


def get_homework(request):
    Homework.objects.get()