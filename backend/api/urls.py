from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MentorshipViewSet, MentorshipSessionViewSet, LearningResourceViewSet

# Créer un routeur par défaut et enregistrer les vues
router = DefaultRouter()
router.register(r'users', UserViewSet,basename="users")
router.register(r'mentorships', MentorshipViewSet,basename="mentorships")
router.register(r'sessions', MentorshipSessionViewSet,basename="sessions")
router.register(r'resources', LearningResourceViewSet,basename="resources")

# Inclure les routes du routeur dans les URLs de l'application
urlpatterns = [
    path('', include(router.urls)),
]