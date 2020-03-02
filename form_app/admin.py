from django.contrib import admin
from form_app.models import FormModel

class FormAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(FormModel, FormAdmin)
