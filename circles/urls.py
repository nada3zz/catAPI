from rest_framework import routers
from django.conf.urls import url,include
from .views import TechCircleViewset, NonTechCircleViewset



router = routers.DefaultRouter()
router.register('techcircle', TechCircleViewset)
router.register('nontechcicle', NonTechCircleViewset)

""""
urlpatterns = [
    url(r'^', include(router.urls)),
 
]
"""