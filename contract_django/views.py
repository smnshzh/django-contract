# views.py

from django.shortcuts import redirect

def custom_page_not_found(request, exception):
    # Redirect to the dashboard page
    return redirect('dashboard')
