from django.contrib import admin
from .models import Role, CodingLang, CourseWork, UserProfile, PlatformName, Certificates, Project

# Register your models here.
admin.site.register(Role)
admin.site.register(CodingLang)
admin.site.register(CourseWork)
admin.site.register(UserProfile)
admin.site.register(PlatformName)
admin.site.register(Certificates)
admin.site.register(Project)
