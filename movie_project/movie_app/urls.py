from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('collection',views.CollectionViewset,basename='create-collection')


urlpatterns=router.urls