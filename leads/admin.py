from django.contrib import admin

from .models import User, SalesPerson, Lead

# Register your models here.
admin.site.register(User)
admin.site.register(SalesPerson)
admin.site.register(Lead)