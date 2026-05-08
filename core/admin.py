from django.contrib import admin

# Register your models here.

from .models import Comments, Contact, Project, Lead

admin.site.register(Comments)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Lead)
