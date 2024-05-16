from django.contrib import admin # type: ignore

# Register your models here.
from . import models

admin.site.register (models.Monoambiente)      
admin.site.register (models.UnDormitorio)
admin.site.register (models.DosDormitorios)
