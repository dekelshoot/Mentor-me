"""
URL configuration for mentor_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api.views import LoginView,ConnexionViewSet,SessionViewSet,RessourceViewSet,EvaluationViewSet,match_mentor_to_mentee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/connexion/', ConnexionViewSet.as_view(), name='connexion'),
    path('api/sessions/', SessionViewSet.as_view(), name='sessions'),
    path('api/ressources/', RessourceViewSet.as_view(), name='ressources'),
    path('api/evaluation/', EvaluationViewSet.as_view(), name='evaluation'),
    path('api/matching/', match_mentor_to_mentee, name='matchin'),
]
