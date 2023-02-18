from apps.school.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'sliders', SliderView, basename='sliders')
router.register(r'partners', PartnerView, basename='partners')
router.register(r'about', AboutView, basename='about')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'courses', CourseView, basename='courses')
router.register(r'news', NewsView, basename='news')
router.register(r'leaders', LeadershipView, basename='leaders')
router.register(r'documents', DocumentView, basename='documents')
