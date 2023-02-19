from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    """View function for displaying and processing login form."""
    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using Django's built-in authentication function
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user is authenticated, log them in and redirect to a success page
            login(request, user)
            return redirect('success')
        else:
            # If the user is not authenticated, return an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # If the request method is GET, render the login form
        return render(request, 'login.html')

def signup_view(request):
    """View function for displaying and processing signup form."""
    if request.method == 'POST':
        # Create a UserCreationForm instance with the data from the POST request
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # If the form is valid, save the user and log them in
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        # If the request method is GET, render the signup form
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    """View function for logging out the user."""
    logout(request)
    return redirect('login')
