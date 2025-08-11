from django.urls import path
from . import views

urlpatterns = [
    # This path will serve your index.html file at the root of your app
    path('', views.index, name='index'),
    # This path maps the form submission endpoint to your view function.
    path('api/submit_registration/', views.submit_registration, name='submit_registration'),
]

