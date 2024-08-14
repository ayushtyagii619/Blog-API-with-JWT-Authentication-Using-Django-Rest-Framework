from django.urls import path
from .views import UserRegistrationApiView,UserLoginApiView,UserLogoutApiView,UserApiView,UserProfileApiView,UserAvtarApiView

urlpatterns = [
    path('register/',UserRegistrationApiView.as_view(),name='register'),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('logout/',UserLogoutApiView.as_view(),name='logout'),
    path('',UserApiView.as_view(),name='user'),
    path('profile/',UserProfileApiView.as_view(),name='profile'),
    path('avtar/',UserAvtarApiView.as_view(),name='avtar'),
] 