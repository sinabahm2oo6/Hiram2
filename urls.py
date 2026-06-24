from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/', views.StudentHomeView.as_view(), name='student_home'),
    path('home/', views.AdminHomeView.as_view(), name='admin_home'),
    path('home/', views.AdvisorHomeView.as_view(), name='advisor_home')
]
