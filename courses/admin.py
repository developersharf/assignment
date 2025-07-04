from django.contrib import admin
from . models import Student, Info
            
# Register your models here.
admin.site.register(Student)

class InfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'batch', 'password', 'textarea')

#     first_name = models.CharField(max_length=35)
#     last_name = models.CharField(max_length=35)
#     email = models.EmailField(max_length=20)
#     batch = models.IntegerField()
#     password = models.CharField(max_length=35)
#     re_password = models.CharField(max_length=35)
#     textarea = models.CharField(max_length=150)

admin.site.register(Info, InfoAdmin)