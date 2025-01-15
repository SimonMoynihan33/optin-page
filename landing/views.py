from django.shortcuts import render
from .models import OptIn  # Import the model

def index(request):
    if request.method == 'POST':
        # Get data from the submitted form
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')

        # Save the data to the database
        OptIn.objects.create(nickname=nickname, email=email)

        # Render a thank-you page after successful submission
        return render(request, 'landing/thank_you.html')

    # Render the main landing page for GET requests
    return render(request, 'landing/index.html')
