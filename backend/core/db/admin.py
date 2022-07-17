from django.contrib import admin


from db.models import Poem


@admin.register(Poem)
class BaseAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
