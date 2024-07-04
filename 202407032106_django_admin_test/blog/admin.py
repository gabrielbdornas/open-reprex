from django.contrib import admin
from . import models

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin area'

blog_site = BlogAdminArea(name='BlogAdmin')

# admin.site.register(models.post)
blog_site.register(models.post)
