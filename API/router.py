from rest_framework import routers
from aboutapi.viewsets import AboutViewset,HistoryViewset,HeadInfoViewset,EventViewset,SessionViewset,TechCircleViewset,NonTechCircleViewset,NewsViewset,TopMemberViewset,BoardViewset

router = routers.DefaultRouter()
router.register('about', AboutViewset) 
router.register('topmember', TopMemberViewset) 
router.register('headinfo', HeadInfoViewset) 
router.register('Techcircle', TechCircleViewset)
router.register('event', EventViewset)
router.register('session', SessionViewset)
router.register('history', HistoryViewset)
router.register('Nontech', NonTechCircleViewset) 
router.register('news', NewsViewset) 
router.register('board', BoardViewset)