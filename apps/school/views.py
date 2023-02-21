from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class AboutView(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SliderView(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    

class PartnerView(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnerSerializer
    

class NewsView(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

class DocumentView(viewsets.ReadOnlyModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    

class AboutView(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    

class LeadershipView(viewsets.ReadOnlyModelViewSet):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
    

class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CategorySerializer
    

class CourseView(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
