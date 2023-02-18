from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import User, Note

# Home
@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        #Getting form fields
        title = request.POST['title']
        description = request.POST['desc']

        if len(title) < 1:
            messages.error(request, "Title is too short!")
        elif len(description) < 1:
            messages.error(request, "Description is too short!")
        else:
            new_note = Note(user_note=request.user, title=title, description=description)
            new_note.save()
            messages.success(request, "Note Added")

    # Filtering notes by recently added
    notes = Note.objects.filter(user_note=request.user).order_by('-date_added')
    return render(request, "core/home.html", {"notes":notes})

#Signup View
def sign_up(request):
    if request.method == 'POST':
        #Getting form fields
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #Check if user exist
        user = User.objects.filter(email=email).exists()

        if user:
            messages.error(request, "Email already exists.")
        elif password1 != password2:
            messages.error(request, "Those passwords didn\'t match. Try again.")
        else:
            #User Registration
            new_user = User.objects.create_user(password=password1,email=email,name=name)
            new_user.save()

            #Authenticating User
            new_user = authenticate(request, email=new_user.email, password=password1)
            if new_user is not None:
                messages.success(request, "Account Created.")
                login(request, new_user)
                return redirect("/")
            else:
                print("user is not authenticated")

    return render(request, "core/signup.html")

#Login View
def login_user(request):
    if request.method == "POST":
        #Getting form fields
        email = request.POST['email']
        password = request.POST['password']

        #Authenticating User
        user = authenticate(request, email=email, password = password)
        if user is not None:
            messages.success(request, "Log In Successful")
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Email does not exist.")

    return render(request, "core/login.html")

#Logout View
def logout_user(request):
    #Sign out user
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("login")

#Delete Note
@login_required(login_url='login')
def delete_note(request, noteID):
    #check if note belog to user
    check_note = get_object_or_404(Note, id=noteID, user_note=request.user)
    check_note.delete()
    messages.success(request, "Note Deleted")
    return redirect("index")
