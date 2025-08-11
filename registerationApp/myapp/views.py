# In your Django app's views.py file
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import TeamRegistration

def index(request):
    """
    Renders the main HTML page for the hackathon registration form.
    """
    return render(request, 'myapp/index.html')

@csrf_exempt
@require_POST
def submit_registration(request):
    try:
        # Get text data from request.POST
        team_name = request.POST.get('teamName')
        contest_theme = request.POST.get('contestTheme')
        
        # Get the uploaded file from request.FILES
        proposal_file = request.FILES.get('proposal_file')

        # Get the JSON data string from the POST request and parse it
        json_data_string = request.POST.get('form_data')
        
        # Create a new model instance and save the data
        registration = TeamRegistration(
            team_name=team_name,
            contest_theme=contest_theme,
            proposal_file=proposal_file,
            form_data=json_data_string # Assign the JSON string to the form_data field
        )
        registration.save()

        return JsonResponse({'success': True, 'message': 'Registration submitted successfully!'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'An unexpected error occurred: {str(e)}'}, status=500)