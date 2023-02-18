# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('sliders/', views.sliders, name='sliders'),
    path('slider_create/', views.slider_create, name='slider_create'),
    path('sliders/<int:pk>', views.slider_detail, name='slider_detail'),
    path('slider_delete/<int:pk>', views.SliderDelete.as_view(), name='slider_delete'),
    path('categories/', views.categories, name='categories'),
    path('category_create/', views.category_create, name='category_create'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('course_by_category/<int:pk>', views.course_by_category, name='course_by_category'),
    path('category_delete/<int:pk>', views.CategoryDelete.as_view(), name='category_delete'),
    path('partners/', views.partners, name='partners'),
    path('partner_create/', views.partner_create, name='partner_create'),
    path('partner/<int:pk>', views.partner_detail, name='partner_detail'),
    path('partner_delete/<int:pk>', views.partnerDelete.as_view(), name='partner_delete'),
    path('courses', views.courses, name='courses'),
    path('course_create', views.course_create, name='course_create'),
    path('course/<int:pk>', views.course_detail, name='course_detail'),
    path('course_delete/<int:pk>', views.courseDelete.as_view(), name='course_delete'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    path('news_create/', views.news_create, name='news_create'),
    path('news_delete/<int:pk>', views.NewsDelete.as_view(), name='news_delete'),
    # path('color_create/<int:pk>', views.color_create, name='color_create'),
    # path('color_delete/<int:pk>', views.ColorDelete.as_view(), name='color_delete'),
]
