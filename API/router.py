from rest_framework import routers
from about.urls import router as aboutrouter
from circles.urls import router as circlesrouter
from events.urls import router as urlsrouter

router = routers.DefaultRouter()

router.registry.extend(aboutrouter.registry)
router.registry.extend(circlesrouter.registry)
router.registry.extend(urlsrouter.registry)