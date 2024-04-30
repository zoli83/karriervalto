from django.contrib import admin

# Register your models here.


from .models import Position, Apply
#from .models import Company

#admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Apply)
