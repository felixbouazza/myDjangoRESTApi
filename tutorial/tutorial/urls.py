from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from user import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('', include('snippets.urls')),
    path('', include(router.urls))
]
