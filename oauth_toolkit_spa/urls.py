from django.urls import path
from .views import LogIn, TokenRefresh, LogOff, LogOffEverywhere,Hello,Flavors, SaveName
from .settings import oauth2_settings

urlpatterns = [
    path('login/', LogIn.as_view()),
    path('refresh/', TokenRefresh.as_view()),
    path('logoff/', LogOff.as_view()),
    path('logoff-everywhere/', LogOffEverywhere.as_view()),
    path('hello/',Hello.as_view()),
    path('flavors/',Flavors.as_view()),
    path('save/',SaveName.as_view())
]
