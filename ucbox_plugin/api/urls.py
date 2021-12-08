from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.APIRootView = views.UCBoxPluginRootView

router.register(r'numbers', views.NumberViewSet)
router.register(r'trunks', views.TrunkViewSet)
router.register(r"ucclusters", views.UCClusterViewSet)
router.register(r"devicepools", views.DevicePoolViewSet)


app_name = "ucbox_plugin-api"
urlpatterns = router.urls
