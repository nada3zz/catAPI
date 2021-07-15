from rest_framework import routers
from .views import AboutViewset, HistoryViewset, NewsViewset


router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('news', NewsViewset) 

