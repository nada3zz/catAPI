from rest_framework import routers
from .views import EventViewset, SessionViewset, EventPhotoViewset



router = routers.DefaultRouter()
router.register('event', EventViewset)
router.register('session', SessionViewset)
router.register('eventphoto', EventPhotoViewset)
