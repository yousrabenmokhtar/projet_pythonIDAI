from django import forms
from .models import Utilisateur
class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['Nom_complet', 'Email_utilisateur', 'photo_profile', 'Description_profile' , 'image_back' , 'bio']

from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['nom_experience', 'Lieu_fonctionnement', 'Duree_experience', 'description']
 
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['nom_etablissement', 'Diplome', 'Annees_Etudes']



from .models import Skills

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['nom_Skill']
 

 
from .models import Langues

class LangueForm(forms.ModelForm):
    class Meta:
        model = Langues
        fields = ['Langue']
 
 

