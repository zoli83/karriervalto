from django.contrib import admin

# Register your models here.

from .models import RegisteredUser, Company, Position, Apply

admin.site.register(RegisteredUser)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Apply)