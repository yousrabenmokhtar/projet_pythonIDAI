from  django.urls import path
from . import views
from .views import *
#from .views import create_experience
#from .views import profile_edit
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>', views.profile, name='profileWithId'),
    path('update_profile/', update_profile, name='update_profile'),
    path('edit_experience/<int:experience_id>/', views.edit_experience, name='edit_experience'),
    path('edit_education/<int:education_id>/', views.edit_education, name='edit_education'),
    path('add_experience/', add_experience, name='add_experience'),
    path('add_sKill/', add_sKill, name='add_sKill'),
    path('add_langue/', views.add_langue, name='add_langue'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_skills/<int:skill_id>/', edit_skills, name='edit_skills'),
    path('choose_skill_to_edit/', choose_skill_to_edit, name='choose_skill_to_edit'),
    path('edit_langue/<int:langue_id>/', edit_langue, name='edit_langue'),
    path('choose_langue_to_edit/', choose_langue_to_edit, name='choose_langue_to_edit'),
    path('choose_education_to_edit/', views.choose_education_to_edit, name='choose_education_to_edit'),
    path('choose_experience_to_edit/', views.choose_experience_to_edit, name='choose_experience_to_edit'),
]
