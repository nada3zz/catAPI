from rest_framework import routers
from .views import AboutViewset, HistoryViewset, NewsAndHomeViewset, HomeViewSet, NewsViewSet


router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('home', NewsAndHomeViewset, basename= 'NewsAndHome') 
router.register('newslist', NewsViewSet)
router.register('homelist', HomeViewSet)
