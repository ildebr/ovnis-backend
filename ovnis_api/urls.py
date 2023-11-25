from django.urls import path
from .views import SightingList, SightingDetail, CommentList, SightingUserList, getMySightings, createSighting, updateSighting, filteredView
from django.conf.urls.static import static
from django.conf import settings
app_name = 'consejo_api'

urlpatterns = [
    path('sightings/', SightingList.as_view(), name="sighting-list"),
    path('sightings/<str:pk>', SightingDetail.as_view(), name="sighting-detail"),
    path('sightings/user/', SightingUserList.as_view(), name="sightings-user"),
    path('comments/<str:pk>', CommentList.as_view(), name="comments"),
    path('mySightings/', getMySightings, name='trying'),
    path('create/', createSighting, name='create-sighting'),
    path('update/<str:pk>', updateSighting.as_view(), name='update'),
    path('sightings/filter/', filteredView.as_view(), name='filter'),
]