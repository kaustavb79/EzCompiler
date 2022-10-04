from django.contrib import admin
from .models import CompilerAPIModel

class CompilerModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

admin.site.register(CompilerAPIModel, CompilerModelAdmin)