# admin.py
from django.contrib import admin
from .models import (
    Profile,
    Service,
    LatestWork,
    Skill,
    TopSkillCategory,
    TopSkillDetails,
    SkillInsightCategory,
    Certificate,
    Project,
    TimeLine,
    ContactUser
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'about_me', 'youtube_link', 'github_link', 'linkedin_link', 'instagram_link', 'connect_title', 'connect_description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')

@admin.register(LatestWork)
class LatestWorkAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'title', 'client_name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TopSkillCategory)
class TopSkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TopSkillDetails)
class TopSkillDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

@admin.register(SkillInsightCategory)
class SkillInsightCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'verify_url')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'github_url', 'linkedin_url')

@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ('year', 'description')

@admin.register(ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
