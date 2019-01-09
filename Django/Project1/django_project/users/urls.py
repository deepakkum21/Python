from django.urls import path
from . import views as user_views
from .views import profile
# django provided views for login and logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),

    # to reset the password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = 'password_reset'),

    # after reset of the password is complete
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name = 'password_reset_complete'),

    # to give confirmation that the link has been sent successfully to the inbox
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),

    # to route to template which PasswordReset sends as it expects 2 parameter uidb64 and token
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm')
]