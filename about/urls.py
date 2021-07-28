from rest_framework import routers
from .views import AboutViewset, HistoryViewset, NewsAndHomeViewset, HomeViewSet, NewsViewSet


router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('news', NewsViewSet)
router.register('home', NewsAndHomeViewset, basename= 'NewsAndHome') 

