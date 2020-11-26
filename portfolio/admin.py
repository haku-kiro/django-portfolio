from django.contrib import admin
from .models import Project

# Import the Project model to the admin page
admin.site.register(Project)