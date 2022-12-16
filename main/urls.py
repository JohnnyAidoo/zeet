from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'message',views.MessagesViewSet, basename='messages')
urlpatterns = router.urls
