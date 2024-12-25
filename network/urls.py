
from django.urls import path

from . import views
from .views import MealPlanView 
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("meal_plan/", MealPlanView.as_view(), name="meal_plan"),
    
    

]
