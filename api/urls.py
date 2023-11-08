from rest_framework import routers
from .views import PostviewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('posts', PostviewSet)

urlpatterns = [
    path('', include(router.urls))
]