from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnerSerializer
    

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

class DocumentView(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    

class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    

class LeadershipView(viewsets.ModelViewSet):
    serializer_class = LeadershipSerializer

    def get_queryset(self):
        queryset = Leadership.objects.all()
        type = self.request.GET.get('type')
        if type == 'leader':
            queryset = queryset.filter(type='Rahbariyat')
        if type == 'employee':
            queryset = queryset.filter(type='Boshqa xodimlar')
        return queryset


class CategoryView(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CategorySerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CourseOwnerView(viewsets.ModelViewSet):
    queryset = CourseOwners.objects.all()
    serializer_class = CourseOwnerSerializer


class PhotoGalleryView(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer


class VideoGalleryView(viewsets.ModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer

