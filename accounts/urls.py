from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('diet/', views.diet, name='diet'),
    path('exercise/', views.exercise, name='exercise'),
    path('recipes/', views.recipes, name='recipes'),
    path('tracker/', views.tracker, name='tracker'),
]

0

