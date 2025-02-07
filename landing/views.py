from django.shortcuts import render
from .forms import OptInForm
from .mailchimp import subscribe_to_mailchimp


def index(request):
    error_message = None  # Default to no error message

    if request.method == "POST":
        form = OptInForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            email = form.cleaned_data['email']

            # Call Mailchimp API
            status, response = subscribe_to_mailchimp(email, nickname)

            if status == 200:
                return render(request, 'landing/thank_you.html')
            else:
                # Extract Mailchimp API error message if available
                error_message = response.get(
                    "detail", "Invalid email address. Please try again.")

    else:
        form = OptInForm()

    return render(
        request, 'landing/index.html', {
            'form': form, 'error': error_message})
