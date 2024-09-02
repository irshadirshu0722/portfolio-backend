# views.py
from rest_framework import generics,viewsets
from rest_framework.response import Response
from .models import (
    Profile,
    Service,
    LatestWork,
    TopSkillCategory,
    SkillInsightCategory,
    Certificate,
    Project,
    TimeLine,
    ContactUser
)
from .serializers import (
    ProfileSerializer,
    ServiceSerializer,
    LatestWorkSerializer,
    TopSkillCategorySerializer,
    SkillInsightCategorySerializer,
    CertificateSerializer,
    ProjectSerializer,
    TimeLineSerializer,
    ContactUserSerializer
)
from rest_framework import status
from rest_framework.views import APIView

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Certificate View
class CertificateListView(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

# Project View
class ProjectListView(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# TimeLine View
class TimeLineListView(viewsets.ReadOnlyModelViewSet):
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer

# ContactUser View
class ContactUserCreateView(generics.CreateAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer


class TopInsightsSkillView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        top_skill_categories = TopSkillCategory.objects.all()
        skill_insight_categories = SkillInsightCategory.objects.all()        
        data = {
            'top_skills': TopSkillCategorySerializer(top_skill_categories, many=True).data,
            'skill_insights': SkillInsightCategorySerializer(skill_insight_categories, many=True).data
        }
        return Response(data)

# homeData View
class HomeDataView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()  # Assuming there is only one profile
        latest_work = LatestWork.objects.all()
        services = Service.objects.all()
        
        data = {
            'profile': ProfileSerializer(profile,context={'request':request}).data,
            'latest_work': LatestWorkSerializer(latest_work, many=True).data,
            'services': ServiceSerializer(services, many=True).data
        }
        return Response(data)

class EnquiryView(APIView):
    def post(self, request):
        try:
            serializer = ContactUserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                name = serializer.validated_data['name']
                email = serializer.validated_data['email']
                subject = serializer.validated_data['subject']
                message = serializer.validated_data['message']
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = settings.EMAIL_TO_MAIL

                html_message = render_to_string(
                    'emails/enquiry_email.html',
                    {
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message,
                    }
                )
                email = EmailMessage(subject, html_message, from_email, [to_email])
                email.content_subtype = 'html'
                try:
                    email.send()
                    return Response({"message": "Enquiry email sent successfully!"}, status=status.HTTP_200_OK)
                except Exception as e:
                    # Log the exception or handle it as needed
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)