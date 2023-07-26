from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('registerstudent/', views.register_student, name='register-student'),
    path('registerteacher/', views.register_teacher, name='register-teacher'),

    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
]
