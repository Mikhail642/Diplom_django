from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth import authenticate



def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))



class Homework(models.Model):
    zagolovok = models.CharField( max_length=200,verbose_name= 'заголовок',)
    Text = models.TextField(verbose_name='Текст',)
    Data_sozdania = models.DateTimeField( default=timezone.now,verbose_name='Дата создания',)
    vypolneno = models.BooleanField('Отметка о выполнении', default=False)
    avtor= models.ForeignKey(User, on_delete=models.CASCADE)

class Partnerorganizations(models.Model):
    nameorganization = models.TextField(verbose_name='Наименование организации',)
    functionorganization = models.TextField(max_length=50, verbose_name='Функции организации в проекте')


class Project_implementation_plan(models.Model):
     zadacha = models.TextField(max_length=150, verbose_name='Задача',)
     srokirealizatchii = models.TextField( max_length=50, verbose_name='СрокиРеализации',)
     otmentaovypolnenii = models.BooleanField('Отметка о выполнении', default=False)



class Publiczna_presentation(models.Model):
    event = models.TextField(max_length=50, verbose_name='Мероприятие',)
    date = models.DateTimeField( default=timezone.now, verbose_name='Дата публикации',)
    form = models.TextField(max_length=50, verbose_name='Форма',)
    place = models.TextField(max_length=50, verbose_name='Место',)
    level = models.TextField(max_length=50, verbose_name='Уровень')



class Prognoz_razvitia_nex_year(models.Model):
   task = models.TextField(max_length=50, verbose_name='Задача',)
   nameProduct = models.TextField(max_length=50, verbose_name='Наименование продукта',)
   kratkoeopisanie = models.TextField(max_length=150, verbose_name='Краткое описание продукта',)
   sokirealizachii = models.TextField(max_length=50, verbose_name='Сроки реализации')

class Product_of_innovation(models.Model):
    productofinnovation = models.TextField(max_length=50, verbose_name='Продукт инновационной деятельности',)
    suggestionsforusingtheresultsobtainedintheregionaleducationsystem=models.TextField( max_length=50, verbose_name='Предложения по использованию результатов проекта полученных  в региональной системе образования')



    def russkoenazvanie(self):
        if self.vypolneno:
            return "Да"
        else :
            return "Нет"


