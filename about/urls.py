from rest_framework import routers
from .views import AboutViewset, HistoryViewset, NewsAndHomeViewset


router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('home', NewsAndHomeViewset, basename= 'NewsAndHome') 

