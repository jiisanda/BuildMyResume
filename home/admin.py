"""
home/admin.py
"""
from django.contrib import admin
from . import models

class ResumeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    search_fields = ['resume_name', ]
    list_filter = ['created_at', ]
    list_display = ['resume_name', 'user', 'created_at', 'updated_at', ]


class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['position', 'company', ]
    lsit_display = ['position', 'company', 'resume', ]


class EducationAdmin(admin.ModelAdmin):
    search_fields = ['school', ]
    list_display = ['school', 'resume', ]


class CertificateAdmin(admin.ModelAdmin):
    search_fields = ['program_name', ]
    list_display = ['program_name', 'resume', ]


class SkillAdmin(admin.ModelAdmin):
    search_fields = ['skill_name', ]
    list_display = ['skill_name', 'resume', ]


class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['language_name', ]
    list_display = ['language_name', 'resume', ]


class CourseworkAdmin(admin.ModelAdmin):
    search_fields = ['coursework_name', ]
    list_display = ['coursework_name', 'resume', ]


admin.site.register(models.ResumeMetaData, ResumeAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Certificate, CertificateAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Coursework, CourseworkAdmin)
