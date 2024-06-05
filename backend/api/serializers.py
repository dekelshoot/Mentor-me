from rest_framework import serializers
from .models import User, Mentorship, MentorshipSession, LearningResource

# Sérialiseur pour le modèle User
class UserSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle User.
    Sérialise tous les champs pertinents d'un utilisateur.
    """
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'username', 'email', 'is_mentor', 'is_mentee', 'age', 'location', 'domain_of_interest', 'level_of_education', 'bio']

# Sérialiseur pour le modèle Mentorship
class MentorshipSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Mentorship.
    Sérialise les détails d'une relation de mentorat.
    """
    class Meta:
        model = Mentorship
        fields = ['id', 'mentor', 'mentee', 'start_date', 'end_date', 'feedback']

# Sérialiseur pour le modèle MentorshipSession
class MentorshipSessionSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle MentorshipSession.
    Sérialise les détails d'une session de mentorat.
    """
    class Meta:
        model = MentorshipSession
        fields = ['id', 'mentorship', 'scheduled_date', 'duration', 'session_type', 'notes']

# Sérialiseur pour le modèle LearningResource
class LearningResourceSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle LearningResource.
    Sérialise les détails d'une ressource d'apprentissage.
    """
    class Meta:
        model = LearningResource
        fields = ['id', 'title', 'description', 'resource_type', 'url']
