
from django.contrib import admin
from blog.templates.blog.models import Partnerorganizations
from blog.templates.blog.models import Project_implementation_plan
from blog.templates.blog.models import Publiczna_presentation
from blog.templates.blog.models import Product_of_innovation
from blog.templates.blog.models import Prognoz_razvitia_nex_year






class PartnerorganizationsAdmin(admin.ModelAdmin):
    list_display = ["nameorganization"]
    list_display_links = ["nameorganization"]



class Project_implementation_planAdmin(admin.ModelAdmin):
    list_display = ["zadacha"]
    list_display_links = ["zadacha"]

    list_display = ["srokirealizatchii"]
    list_display_links = ["srokirealizatchii"]

    list_display = ["otmentaovypolnenii"]
    list_display_links = ["otmentaovypolnenii"]

class Publiczna_presentationAdmin(admin.ModelAdmin):
    list_display = ["event"]
    list_display_links = ["event"]

    list_display = ["date"]
    list_display_links = ["date"]

    list_display = ["form"]
    list_display_links = ["form"]

    list_display = ["place"]
    list_display_links = ["place"]

    list_display = ["level"]
    list_display_links = ["level"]




class Prognoz_razvitia_nex_yearAdmin(admin.ModelAdmin):
    list_display = ["task"]
    list_display_links = ["task"]

    list_display = ["nameproduct"]
    list_display_links = ["nameproduct"]

    list_display = ["kratkoeopisanie"]
    list_display_links = ["kratkoeopisanie"]


    list_display = ["sokirealizachii"]
    list_display_links = ["sokirealizachii"]

class Product_of_innovationAdmin(admin.ModelAdmin):
    list_display = ["productofinnovation"]
    list_display_links = ["productofinnovation"]

    list_display = ["suggestionsforusingtheresultsobtainedintheregionaleducationsystem"]
    list_display_links = ["suggestionsforusingtheresultsobtainedintheregionaleducationsystem"]



admin.site.register(Partnerorganizations, PartnerorganizationsAdmin)

admin.site.register(Project_implementation_plan, Project_implementation_planAdmin)

admin.site.register(Publiczna_presentation,Publiczna_presentationAdmin)


admin.site.register(Product_of_innovation, Product_of_innovationAdmin)

admin.site.register(Prognoz_razvitia_nex_year, Prognoz_razvitia_nex_yearAdmin)
