from django.urls import path
from .views import CustomUserCreate, UserList, UserDetail, CurrentUser, getNotes, createSighting, updateSighting

app_name= 'users'

urlpatterns = [
	path('register/', CustomUserCreate.as_view(), name="create_user"),
	path('<int:pk>', UserDetail.as_view(), name="user_detail" ),
	path('', CurrentUser.as_view(), name="current_user" ),
    path('me/', CurrentUser.as_view(), name="user_list" ),
    


    path('trying/', getNotes, name='trying'),
    path('createsigh', createSighting, name='create-sighting'),
    path('update/<str:pk>', updateSighting.as_view(), name='update'),
]