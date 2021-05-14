
from rest_framework import routers
from aboutapi.viewsets import AboutViewset, HistoryViewset, NewsViewset
from events.views import EventViewset, SessionViewset, EventPhotoViewset
from circles.views import TechCircleViewset, NonTechCircleViewset

router = routers.DefaultRouter()
router.register('about', AboutViewset)
router.register('history', HistoryViewset) 
router.register('news', NewsViewset) 
router.register('event', EventViewset)
router.register('session', SessionViewset)
router.register('eventphoto', EventPhotoViewset)
router.register('Techcircle', TechCircleViewset)
router.register('Nontechcicle', NonTechCircleViewset) 
#router.register('topmember', TopMemberViewset) 
#router.register('headinfo', HeadInfoViewset) 
#router.register('board', BoardViewset)

