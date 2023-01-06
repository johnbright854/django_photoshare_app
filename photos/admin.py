from django.contrib import admin
from .models import Photo,Category
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class adminlog(admin.ModelAdmin):
    pass 

admin.site.register(Category,adminlog)
admin.site.register(Photo,adminlog)
