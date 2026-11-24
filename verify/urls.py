from django.urls import path, include
from .views import *
urlpatterns = [
    path('', registration, name="registration"),
    path("confirm_email/", confirm_email, name="confirm_email"),
    path("login/", login_user, name="login"),
    path('home/',home, name='home'),
    path("profile/", show_profile, name="profile"), 
    path('logout/', logout_user, name='logout'),
    path('profile/', show_profile, name='profile'),
    path('tasks/',tasks, name='tasks'),
    path('tasks/add/',add_task, name='add_task'),
    path('tasks/edit/<int:id>/',edit_task, name='edit_task'),
    path('tasks/delete/<int:id>/',delete_task, name='delete_task'),
    path('send-hello/', send_hello, name='send_hello'),
    path('res/', res, name='res')
    ]