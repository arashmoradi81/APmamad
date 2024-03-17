from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/signup/', SignupView.as_view(), name='signup'),
]
