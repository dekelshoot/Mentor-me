from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle utilisateur personnalisé (Mentor et Mentee)
class User(AbstractUser):
    """
    Modèle utilisateur personnalisé (Mentor et Mentee).
    Attributs supplémentaires :
    - is_mentor : booléen indiquant si l'utilisateur est un mentor.
    - is_mentee : booléen indiquant si l'utilisateur est un mentee.
    - age : âge de l'utilisateur.
    - location : emplacement géographique de l'utilisateur.
    - domain_of_interest : domaine d'intérêt de l'utilisateur.
    - level_of_education : niveau d'éducation de l'utilisateur.
    - bio : biographie de l'utilisateur.
    """
    is_mentor = models.BooleanField(default=False)  # Indique si l'utilisateur est un mentor
    is_mentee = models.BooleanField(default=False)  # Indique si l'utilisateur est un mentee
    age = models.IntegerField(null=True, blank=True)  # Âge de l'utilisateur
    location = models.CharField(max_length=100, null=True, blank=True)  # Emplacement géographique de l'utilisateur
    domain_of_interest = models.CharField(max_length=100, null=True, blank=True)  # Domaine d'intérêt de l'utilisateur
    level_of_education = models.CharField(max_length=100, null=True, blank=True)  # Niveau d'éducation de l'utilisateur
    bio = models.TextField(null=True, blank=True)  # Biographie de l'utilisateur

    def __str__(self):
        return self.username

# Modèle pour représenter une relation de mentorat
class Mentorship(models.Model):
    """
    Modèle pour représenter une relation de mentorat.
    Attributs :
    - mentor : référence au mentor.
    - mentee : référence au mentee.
    - start_date : date de début de la relation de mentorat.
    - end_date : date de fin de la relation de mentorat (si applicable).
    - feedback : feedback sur la relation de mentorat.
    """
    mentor = models.ForeignKey(User, related_name='mentorships_as_mentor', on_delete=models.CASCADE)  # Référence au mentor
    mentee = models.ForeignKey(User, related_name='mentorships_as_mentee', on_delete=models.CASCADE)  # Référence au mentee
    start_date = models.DateField(auto_now_add=True)  # Date de début de la relation de mentorat
    end_date = models.DateField(null=True, blank=True)  # Date de fin de la relation de mentorat (si applicable)
    feedback = models.TextField(null=True, blank=True)  # Feedback sur la relation de mentorat

    def __str__(self):
        return f'{self.mentor.username} mentors {self.mentee.username}'

# Modèle pour les sessions de mentorat
class MentorshipSession(models.Model):
    """
    Modèle pour les sessions de mentorat.
    Attributs :
    - mentorship : référence à la relation de mentorat.
    - scheduled_date : date et heure de la session de mentorat.
    - duration : durée de la session (ex. 1 heure).
    - session_type : type de session (individuelle, groupe, webinaire).
    - notes : notes prises pendant la session.
    """
    mentorship = models.ForeignKey(Mentorship, related_name='sessions', on_delete=models.CASCADE)  # Référence à la relation de mentorat
    scheduled_date = models.DateTimeField()  # Date et heure de la session de mentorat
    duration = models.DurationField()  # Durée de la session (ex. 1 heure)
    session_type = models.CharField(max_length=50)  # Type de session (individuelle, groupe, webinaire)
    notes = models.TextField(null=True, blank=True)  # Notes prises pendant la session

    def __str__(self):
        return f'Session on {self.scheduled_date} for {self.mentorship}'

# Modèle pour les ressources d’apprentissage
class LearningResource(models.Model):
    """
    Modèle pour les ressources d’apprentissage.
    Attributs :
    - title : titre de la ressource.
    - description : description de la ressource.
    - resource_type : type de ressource (article, vidéo, cours).
    - url : URL de la ressource.
    """
    title = models.CharField(max_length=200)  # Titre de la ressource
    description = models.TextField()  # Description de la ressource
    resource_type = models.CharField(max_length=50)  # Type de ressource (article, vidéo, cours)
    url = models.URLField()  # URL de la ressource

    def __str__(self):
        return self.title
