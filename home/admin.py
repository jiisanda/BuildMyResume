from django.contrib import admin
from .models import Profile, Social, Education, Skill, CodingLang, CourseWork, PlatformName, Certificates, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(CodingLang)
admin.site.register(CourseWork)
admin.site.register(PlatformName)
admin.site.register(Certificates)
admin.site.register(Project)
