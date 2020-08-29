from rest_framework.routers import SimpleRouter
from appone import views

router=SimpleRouter()
router.register('api/v1',views.Productview)

urlpatterns = router.urls