
from django.contrib import admin
from .models import TeamRegistration

@admin.register(TeamRegistration)
class TeamRegistrationAdmin(admin.ModelAdmin):
    # This list controls which fields are displayed in the main list view of the admin page
    list_display = ('team_name', 'contest_theme', 'submission_date')
    
    # This list enables filtering in the admin panel by contest theme
    list_filter = ('contest_theme', 'submission_date')
    
    # This enables a search bar to search through team names and themes
    search_fields = ('team_name', 'contest_theme')
    
    # This makes the form_data field read-only and formats it nicely
    readonly_fields = ('submission_date', 'form_data')
    
    # Optional: Customize the order of fields in the detail view
    fieldsets = (
        (None, {
            'fields': ('team_name', 'contest_theme', 'submission_date')
        }),
        ('Full Form Data (JSON)', {
            'fields': ('form_data',)
        }),
    )

