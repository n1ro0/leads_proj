from django.contrib import admin


from . import models


admin.site.register((models.Lead, models.Language))
