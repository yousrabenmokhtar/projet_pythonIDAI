from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('home/' , views.home , name = 'home'),
    path('' , views.Sign , name = 'sign' ),
    path('logout/' , views.logoutUser , name = 'logout'),
    path('laureats/', views.laureat, name='laureat'),
    path('profile/<str:nom_complet>/', views.user_profile, name='user_profile'),

    path('profile_Lists/', views.profile_Lists , name = 'profile_Lists'),
    path('<int:post_id>/like/', views.like, name='like'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='pages/reset_password.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='pages/password_update.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='pages/reset_password_complete.html'), name='password_reset_complete'),

    
]

