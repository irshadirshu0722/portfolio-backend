from rest_framework import serializers
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
    ContactUser,
    ContactUser
)

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# TopSkillDetails Serializer
class TopSkillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSkillDetails
        fields = '__all__'

# TopSkillCategory Serializer
class TopSkillCategorySerializer(serializers.ModelSerializer):
    skills = TopSkillDetailsSerializer(many=True, read_only=True)
    class Meta:
        model = TopSkillCategory
        fields = '__all__'

# SkillInsightCategory Serializer
class SkillInsightCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = SkillInsightCategory
        fields = '__all__'

# Certificate Serializer
class CertificateSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    image_url  = serializers.SerializerMethodField()
    class Meta:
        model = Certificate
        fields = '__all__'
    def get_image_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ3tZfSplP0w6l3lkvCQ57yGpALJ7hNm-zJg&s"
        return request.build_absolute_uri(obj.image_url.url)

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
    
# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    hero_image = serializers.SerializerMethodField()
    about_image = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = '__all__'
    def get_hero_image(self,obj):
        request = self.context.get('request')
        if request is None:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ3tZfSplP0w6l3lkvCQ57yGpALJ7hNm-zJg&s"
        return request.build_absolute_uri(obj.hero_image.url)
    def get_about_image(self,obj):
        request = self.context.get('request')
        if request is None:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ3tZfSplP0w6l3lkvCQ57yGpALJ7hNm-zJg&s"
        return request.build_absolute_uri(obj.about_image.url)

# Service Serializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

# LatestWork Serializer
class LatestWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestWork
        fields = '__all__'

# TimeLine Serializer
class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = '__all__'

# ContactUser Serializer
class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUser
        fields = '__all__'
