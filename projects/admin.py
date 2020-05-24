from django.contrib import admin
from .models import Project, Photo
# Register your models here.

#customizing admin interface
admin.site.site_header = "Gateway 47 startup admin"
admin.site.site_title = "Gateway 47 - startup"
admin.site.index_title = "Gateway47 startup"

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Project, ProjectAdmin)