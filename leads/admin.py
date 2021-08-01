from django.contrib import admin

from .models import User, SalesPerson, Lead, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(SalesPerson)
admin.site.register(Lead)
admin.site.register(UserProfile)