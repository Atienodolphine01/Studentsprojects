from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.registration, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('new-project/', views.postproject, name='newproject'),
    path('project/<id>', views.get_project, name='project'),
    path('search', views.search_projects, name='search'),
    
]