from django.urls import path
from .views import landing_page, add_student, success  


urlpatterns = [
    path('', landing_page, name='landing'),  # Landing page route
    path('add-student/', add_student, name='add_student'),  # Add student form route
    path('success/', success, name='success'),
]

