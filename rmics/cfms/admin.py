from django.contrib import admin
from .models import FindingsLog



class FindingsLogAdmin(admin.ModelAdmin):
    list_display = (
        'findings_title',
        'timestamp',
    )

admin.site.register(FindingsLog, FindingsLogAdmin)


# Register your models here.
