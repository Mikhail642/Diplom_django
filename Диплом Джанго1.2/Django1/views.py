# Create your views here.
from blog.models import Homework


def get_homework(request):
    Homework.objects.get()