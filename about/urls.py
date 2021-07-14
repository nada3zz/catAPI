from rest_framework import routers
from django.conf.urls import url,include
from .views import AboutViewset, HistoryViewset, NewsViewset


router = routers.DefaultRouter()
router.register(r'about', AboutViewset)
router.register(r'history', HistoryViewset) 
router.register(r'news', NewsViewset) 

"""
urlpatterns = [
    url(r'^', include(router.urls)),
 
]
"""