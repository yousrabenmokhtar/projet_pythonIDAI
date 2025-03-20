from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):

    # username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nom Complet...'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email...'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe...'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmation du mot de passe...'}))

    Roles = (
        ('Etudiant', 'Etudiant'),
        ('Professeur', 'Professeur'),
        ('Entreprise', 'Entreprise'),
    )
    role = forms.ChoiceField(choices=Roles)
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2' , 'role']

        widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'password1': forms.PasswordInput(attrs={'class': 'role-select', 'placeholder': 'Password'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
}


# class PublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ['contenu', 'image_publication', 'video_publication', 'document_publication']  # Include 'document_publication' field


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['contenu', 'image_publication', 'video_publication', 'document_publication']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['publication', 'contenu_commentaire']  # Ajoutez le champ 'publication' à votre formulaire

    # Ajoutez un champ de formulaire caché pour le champ 'publication_id'
    publication_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    # Mettez à jour la méthode __init__ pour initialiser la valeur de 'publication_id' si elle est fournie
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['publication_id'].initial = kwargs['instance'].publication_id

    # Mettez à jour la méthode save pour attribuer la valeur 'publication_id' à la relation ForeignKey 'publication'
    def save(self, commit=True):
        instance = super(CommentForm, self).save(commit=False)
        instance.publication_id = self.cleaned_data['publication_id']
        if commit:
            instance.save()
        return instance