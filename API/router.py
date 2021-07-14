#from rest_framework import routers
from django.conf.urls import url,include


urlpatterns = [
    url(r'^about/', include('about.urls')), 
    url(r'^/circles', include('circles.urls')), 
    url(r'^/events', include('events.urls')),

]





"""
from rest_framework import routers
from about.viewsets import AboutViewset, HistoryViewset, NewsViewset
from events.views import EventViewset, SessionViewset, EventPhotoViewset
from circles.views import TechCircleViewset, NonTechCircleViewset

router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('news', NewsViewset) 
router.register('event', EventViewset)
router.register('session', SessionViewset)
router.register('eventphoto', EventPhotoViewset)
router.register('techcircle', TechCircleViewset)
router.register('nontechcicle', NonTechCircleViewset) 
"""


