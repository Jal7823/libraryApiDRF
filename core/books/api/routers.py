from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewsSets.viewsBooks import BooksViewSets
from .viewsSets.viewsAuthor import AuthorViewSets
from .viewsSets.viewsCategory import CategoryViewSets
from .viewsSets.viewsEditorial import EditorialViewSets


router = DefaultRouter()
router.register(r'books',BooksViewSets,basename='books',tags='ksljdklsajldlk')
router.register(r'author',AuthorViewSets,basename='author')
router.register(r'editorial',EditorialViewSets,basename='editorial')
router.register(r'category',CategoryViewSets,basename='category')


urlpatterns = [
    path('', include(router.urls)),
]