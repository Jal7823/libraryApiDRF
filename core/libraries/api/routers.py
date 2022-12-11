from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LibraryViewSets


router = DefaultRouter()
router.register(r'Library',LibraryViewSets,basename='library')

urlpatterns = [
    path('', include(router.urls)),
]