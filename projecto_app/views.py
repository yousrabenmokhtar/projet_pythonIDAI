from django.shortcuts import render,redirect
from .models import *
from .forms import UtilisateurForm
from .forms import ExperienceForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Experience
from myApp.models import Publication
def profile(request, id=None):

    currentUser = request.user
    utiliExcluded = Utilisateur.objects.exclude(user = currentUser)

    
    if id:
      utilisateur = Utilisateur.objects.get(id=id)
    else:
      utilisateur = Utilisateur.objects.get(user=request.user)


    monProfile = False
    if request.user == utilisateur.user:
        monProfile = True


    # Récupérer l'utilisateur actuellement connecté ou le user dont vous voulez afficher le profil
    # utilisateur = Utilisateur.objects.get(user=request.user)
    # Récupérer les informations d'éducation de l'utilisateur
    educations = Education.objects.filter(utilisateur=utilisateur)
    # Récupérer les compétences de l'utilisateur
    skills = Skills.objects.filter(utilisateur=utilisateur)
    langues = Langues.objects.filter(utilisateur=utilisateur)
    # Récupérer l'expérience professionnelle de l'utilisateur
    experiences = Experience.objects.filter(utilisateur=utilisateur)
    context = {
        
        'utilisateur': utilisateur,
        'educations': educations,
        'monProfile' : monProfile,
        'skills': skills,
        'langues': langues,
        'experiences': experiences,
        'utiliExcluded': utiliExcluded,
    }
    return render(request, 'pages/profile.html', context)
# views.py
def update_profile(request):
    utilisateur = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, request.FILES, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UtilisateurForm(instance=utilisateur)
    
    context = {
        'form': form
    }
    return render(request, 'pages/update_profile.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from .models import Experience
from .forms import ExperienceForm

def edit_experience(request, experience_id):# Définition de la vue edit_experience prenant l'ID de l'expérience en paramètre
    experience =  Experience.objects.get(id=experience_id)#Récupération de l'expérience à modifier ou 404 si non trouvée
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'pages/edit_experience.html', {'form': form})

from .forms import EducationForm

def edit_education(request, education_id):# Définition de la vue edit_experience prenant l'ID de l'expérience en paramètre
    education = Education.objects.get(id=education_id)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Rediriger vers la page de profil après la modification
    else:
        form = EducationForm(instance=education)
    return render(request, 'pages/edit_education.html', {'form': form})



def add_experience(request):
    if request.method == 'POST':
        nom_experience = request.POST.get('nom_experience')
        description = request.POST.get('description')
        Lieu_fonctionnement = request.POST.get('Lieu_fonctionnement')

        # Récupérer l'utilisateur actuel
        utilisateur = Utilisateur.objects.get(user=request.user)
        # Créer une nouvelle expérience associée à cet utilisateur
        Experience.objects.create(nom_experience=nom_experience, description=description,Lieu_fonctionnement=Lieu_fonctionnement,utilisateur=utilisateur)
        return redirect('profile')  
    return render(request, 'pages/add_experience.html')  

from .forms import SkillForm


def add_sKill(request):
    if request.method == 'POST':
        nom_Skill = request.POST.get('nom_Skill')
       
        # Récupérer l'utilisateur actuel
        utilisateur = Utilisateur.objects.get(user=request.user)
        # Créer une nouvelle expérience associée à cet utilisateur
        Skills.objects.create(nom_Skill=nom_Skill,utilisateur=utilisateur)
        return redirect('profile')  # Rediriger vers la page du profil de l'utilisateur
    return render(request, 'pages/add_skill.html')  

def add_langue(request):
    if request.method == 'POST':
        Langue = request.POST.get('Langue')
       
        # Récupérer l'utilisateur actuel
        utilisateur = Utilisateur.objects.get(user=request.user)
        # Créer une nouvelle expérience associée à cet utilisateur
        Langues.objects.create(Langue=Langue,utilisateur=utilisateur)
        return redirect('profile')  
    return render(request, 'pages/add_langue.html')  

def add_education(request):
    if request.method == 'POST':
        Diplome = request.POST.get('Diplome')
        nom_etablissement = request.POST.get('nom_etablissement')
        Annees_Etudes = request.POST.get('Annees_Etudes')
        utilisateur = Utilisateur.objects.get(user=request.user)
        Education.objects.create(Diplome=Diplome, nom_etablissement=nom_etablissement,Annees_Etudes=Annees_Etudes,utilisateur=utilisateur)
        return redirect('profile')  
    return render(request, 'pages/add_education.html')  

def edit_skills(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirigez vers une page appropriée après la modification
    else:
        form = SkillForm(instance=skill)
    
    return render(request, 'pages/edit_skills.html', {'form': form})
from django.shortcuts import render
from .forms import LangueForm

def choose_skill_to_edit(request):
    utilisateur = Utilisateur.objects.get(user=request.user)
    skills = Skills.objects.filter(utilisateur=utilisateur)
    return render(request, 'pages/choose_skill_to_edit.html', {'skills': skills})


# langue
def edit_langue(request, langue_id):
    langues = Langues.objects.get(id=langue_id)
    if request.method == 'POST':
        form = LangueForm(request.POST, instance=langues)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirigez vers une page appropriée après la modification
    else:
        form = LangueForm(instance=langues)
    
    return render(request, 'pages/edit_langue.html', {'form': form})



def choose_langue_to_edit(request):
    utilisateur = Utilisateur.objects.get(user=request.user)
    langues = Langues.objects.filter(utilisateur=utilisateur)
    return render(request, 'pages/choose_langue_to_edit.html', {'langues': langues})


def choose_education_to_edit(request):
    utilisateur = Utilisateur.objects.get(user=request.user)
    educations = Education.objects.filter(utilisateur=utilisateur)
    return render(request, 'pages/choose_education_to_edit.html', {'educations': educations})

def choose_experience_to_edit(request):
    utilisateur = Utilisateur.objects.get(user=request.user)
    experiences = Experience.objects.filter(utilisateur=utilisateur)
    return render(request, 'pages/choose_experience_to_edit.html', {'experiences': experiences})
# Dans votre fichier views.py