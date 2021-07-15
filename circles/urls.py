from rest_framework import routers
from .views import TechCircleViewset, NonTechCircleViewset



router = routers.DefaultRouter()
router.register('techcircle', TechCircleViewset)
router.register('nontechcicle', NonTechCircleViewset)

