from django.shortcuts import render
from .forms import OptInForm

def index(request):
    if request.method == "POST":
        form = OptInForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            email = form.cleaned_data['email']
            
            # Logic for storing or sending email data (e.g., to Mailchimp)

            return render(request, 'landing/thank_you.html')
    else:
        form = OptInForm()

    return render(request, 'landing/index.html', {'form': form})
