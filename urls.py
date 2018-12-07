from django.urls import path, include

import calories.views
import frontend.views

urlpatterns = [
    path('', frontend.views.index),
    path('counter/', calories.views.calories),
    #path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/login/', frontend.views.login),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', frontend.views.register)
]
