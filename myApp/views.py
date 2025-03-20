from django.shortcuts import render, redirect
from .forms import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .decorations import *
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def logoutUser(request):
  logout(request)
  return redirect('sign')



def all_publications(request):
    publications = Publication.objects.order_by('-date_publication')
    return render(request, 'pages/home.html', {'publications': publications})

# def get_all_publications():
#     return Publication.objects.all()

# from django.shortcuts import render
# from .models import Publication

# def home_view(request):
#     publications = Publication.objects.get_all_publications()
#     return render(request, 'home.html', {'publications': publications})



# def create_publication(request):
#     if request.method == 'POST':
#         form = PublicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             publication = form.save(commit=False)
#             utilisateur_instance = Utilisateur.objects.get(Nom_complet="Moutaouakel")
           

#             publication.auteur = utilisateur_instance
#             publication.save()
#             return redirect('home')
#     else:
#         form = PublicationForm()
#     return render(request, 'pages/home.html', {'form': form})




# def add_comment(request):
#     if request.method == 'POST':
#         publication_id = request.POST.get('publication_id')
#         comment_content = request.POST.get('comment')
        
#         utilisateur_instance = Utilisateur.objects.get(Nom_complet="Moutaouakel")
#         # Create the comment
#         Commentaire.objects.create(
#             utilisateur=utilisateur_instance,
#             publication_id=publication_id,
#             contenu_commentaire=comment_content
#         )
        
#         # Redirect back to the same page or wherever you want
#         return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
#     else:
#         # Handle GET requests if needed
#         pass


# a function that can do both things : sign & login




@unauthenticatedUser
def Sign(request):
    if request.method == 'POST':
        if 'sign_in' in request.POST:
            # Vérification pour la connexion
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email or Password is not correct !")
        elif 'sign_up' in request.POST:
            # Gestion de l'inscription
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                role = form.cleaned_data.get('role')
                group = Group.objects.get(name=role)
                password = form.cleaned_data.get('password1')
                user.groups.add(group)
                Utilisateur.objects.create(user=user, user_type=role, Nom_complet=user.username, Email_utilisateur=user.email, Password_utilisateur=password)
                messages.success(request, f'Account created for {role}: {user.username}')
                return redirect('sign')
            else:
                # Si le formulaire n'est pas valide, renvoyer le formulaire avec les erreurs
                messages.error(request, "Error creating account. Please check the form data.")
                # Redéfinir le formulaire ici pour le renvoyer avec les erreurs
                form = CreateUserForm(request.POST)
    else:
        # Création d'une instance de formulaire vide pour afficher dans le cas GET
        form = CreateUserForm()

    return render(request, 'pages/sign.html', {'form': form})



def laureat(request):

    return render(request , 'pages/laureat.html')

@login_required(login_url='sign.html')
def home(request):
    if request.method == 'POST':
        # Vérifiez si le formulaire de création de publication a été soumis
        publication_form = PublicationForm(request.POST, request.FILES)
        if publication_form.is_valid():
            publication = publication_form.save(commit=False)
            publication.auteur = request.user.utilisateur
            publication.save()
            # Rediriger l'utilisateur vers la page d'accueil après avoir ajouté la publication
            return redirect('home')

    # Récupérez toutes les publications existantes pour afficher sur la page d'accueil
    publications = Publication.objects.order_by('-date_publication')

    # Récupérez l'utilisateur connecté s'il est authentifié
    if request.user.is_authenticated:
        utilisateur = request.user.utilisateur
        followers_counts = Utilisateur.objects.filter(follows=utilisateur).count()
        following_counts = utilisateur.follows.count()
        allusers = Utilisateur.objects.all()
        posts_count = Publication.objects.filter(auteur=utilisateur).count()
        users = Utilisateur.objects.exclude(id=utilisateur.id)
    else:
        utilisateur = None
        users = Utilisateur.objects.all()
        followers_counts = 0
        following_counts = 0
        allusers = []

    # Créez une instance du formulaire de publication vide pour afficher dans le template
    publication_form = PublicationForm()

    context = {
        'users': users,
        'utilisateur': utilisateur,
        'publications': publications,
        'allusers': allusers,
        'posts_count': posts_count,
        'following_counts': following_counts,
        'followers_counts': followers_counts,
        'publication_form': publication_form,  # Ajoutez le formulaire de publication au contexte
    }

    return render(request, 'pages/home.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Utilisateur

def user_profile(request, nom_complet):
    user = get_object_or_404(Utilisateur, Nom_complet=nom_complet)
    # Ajoutez ici le code pour récupérer les informations du profil de l'utilisateur
    return render(request, 'pages/profile.html', {'user': user})





from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm, CommentForm
















def profile_Lists(request):

    currentUser = request.user
    utilisateur = Utilisateur.objects.exclude(user = currentUser)


    return render(request , 'pages/profile_list.html', {"utilisateur": utilisateur} )


def like(request, post_id):
    utilisateur = Utilisateur.objects.get(user=request.user)
    publication = get_object_or_404(Publication, id=post_id)
    current_likes = publication.Nombre_like
    liked = Likes.objects.filter(user=utilisateur, post=publication).count()

    if not liked:
        Likes.objects.create(user=utilisateur, post=publication)
        current_likes += 1
    else:
        Likes.objects.filter(user=utilisateur, post=publication).delete()
        current_likes -= 1
        
    publication.Nombre_like = current_likes
    publication.save()
    
    # Redirect to the home page after like/unlike
    return HttpResponseRedirect(reverse('home'))

