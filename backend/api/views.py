from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Mentorship, MentorshipSession, LearningResource
from .serializers import UserSerializer, MentorshipSerializer, MentorshipSessionSerializer, LearningResourceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Vue pour le modèle User.
    Fournit des opérations CRUD pour les utilisateurs.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MentorshipViewSet(viewsets.ModelViewSet):
    """
    Vue pour le modèle Mentorship.
    Fournit des opérations CRUD pour les relations de mentorat.
    """
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer

class MentorshipSessionViewSet(viewsets.ModelViewSet):
    """
    Vue pour le modèle MentorshipSession.
    Fournit des opérations CRUD pour les sessions de mentorat.
    """
    queryset = MentorshipSession.objects.all()
    serializer_class = MentorshipSessionSerializer

class LearningResourceViewSet(viewsets.ModelViewSet):
    """
    Vue pour le modèle LearningResource.
    Fournit des opérations CRUD pour les ressources d'apprentissage.
    """
    queryset = LearningResource.objects.all()
    serializer_class = LearningResourceSerializer

