# from django.urls import path
# from . import api_views  

# urlpatterns = [
#     path('api/authors', api_views.AllAuthor.as_view(), name='authors'),
#     path('api/posts', api_views.AllPost.as_view(), name='posts'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'authors/hello',api_views.AuthorViewSet)
router.register(r'posts',api_views.PostViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
]
