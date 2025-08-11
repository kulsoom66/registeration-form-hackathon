from django.db import models
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

class TeamRegistration(models.Model):
    """
    A single entry to store all data for a team's hackathon registration.
    """
    # ... (existing fields)
    team_name = models.CharField(max_length=255)
    contest_theme = models.CharField(max_length=255)
    submission_date = models.DateTimeField(default=timezone.now)

    # Use a JSONField to store the entire form data as a single object.
    form_data = models.TextField()

    # The new FileField to store the uploaded PDF.
    proposal_file = models.FileField(upload_to='proposals/')

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = 'Team Registration'
        verbose_name_plural = 'Team Registrations'
        ordering = ['-submission_date']