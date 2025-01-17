from django.shortcuts import render
from .forms import OptInForm
from .mailchimp import subscribe_to_mailchimp

def index(request):
    if request.method == "POST":
        form = OptInForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            email = form.cleaned_data['email']

            # Call Mailchimp API
            status, response = subscribe_to_mailchimp(email, nickname)
            if status == 200:
                # Redirect to thank you page on successful subscription
                return render(request, 'landing/thank_you.html')
            else:
                # Handle Mailchimp errors
                error_message = response.get("detail", "An error occurred while signing up.")
                return render(request, 'landing/index.html', {'form': form, 'error': error_message})
    else:
        form = OptInForm()

    return render(request, 'landing/index.html', {'form': form})
