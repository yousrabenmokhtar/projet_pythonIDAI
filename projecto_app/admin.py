from django.contrib import admin
from .models import Utilisateur, Education, Skills, Langues, Experience

# Register your models here.
# admin.site.register(Utilisateur)
admin.site.register(Education),
admin.site.register(Skills),
admin.site.register(Langues),
admin.site.register(Experience),
