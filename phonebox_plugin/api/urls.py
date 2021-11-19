from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.APIRootView = views.UCBoxPluginRootView

router.register(r'numbers', views.NumberViewSet)
router.register(r'trunks', views.TrunkViewSet)

app_name = "ucbox_plugin-api"
urlpatterns = router.urls
