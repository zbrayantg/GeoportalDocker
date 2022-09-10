from django.contrib import admin
from .models import Property
# Register your models here.


class InmuebleAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ("predial", "document_number", "real_state_register")
    list_filter = ["act", ]


admin.site.register(Property, InmuebleAdmin)
