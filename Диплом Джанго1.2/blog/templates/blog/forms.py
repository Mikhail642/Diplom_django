from django import forms


class Partnerorganizations(forms.Form):
    nameorganization = forms.CharField()
    functionorganization = forms.CharField()

class Project_implementation_plan(forms.Form):
    zadacha = forms.CharField()
    srokirealizatchii = forms.CharField()
    otmentaovypolnenii = forms.CharField()

class Publiczna_presentation(forms.Form):
    event = forms.CharField()
    date = forms.CharField()
    form = forms.CharField()
    place = forms.CharField()
    level = forms.CharField()

class Prognoz_razvitia_nex_year(forms.Form):
    task = forms.CharField()
    nameProduct = forms.CharField()
    kratkoeopisanie = forms.CharField()

class Product_of_innovation(forms.Form):
    productofinnovation = forms.CharField()
    suggestionsforusingtheresultsobtainedintheregionaleducationsystem = forms.CharField()
