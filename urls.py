from django.contrib.auth.views import LoginView
from django.urls import path, include

import calories.views
import frontend.views

urlpatterns = [
    path('', frontend.views.index),
    path('counter/', calories.views.calories),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', frontend.views.register)
]
