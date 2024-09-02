from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactUserCreateView,
    HomeDataView,
    TopInsightsSkillView,
    CertificateListView,
    ProjectListView,
    TimeLineListView,
    EnquiryView

)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'certificates', CertificateListView, basename='certificate')
router.register(r'projects', ProjectListView, basename='project')
router.register(r'time-lines', TimeLineListView, basename='time-line')

# The router generates URLs for the viewsets
urlpatterns = [
    path('', include(router.urls)),  # Includes the router-generated URLs
    path('contact/', ContactUserCreateView.as_view(), name='contact-user-create'),
    path('home-data/', HomeDataView.as_view(), name='home-data'),
    path('top-insights-skill/', TopInsightsSkillView.as_view(), name='top-insights-skill'),
    path('enquiry/', EnquiryView.as_view(), name='enquiry'),
]
