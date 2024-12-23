from django.contrib import admin

from .models import Employee, Store


# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
