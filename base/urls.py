from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('registerstudent/', views.register_student, name='register-student'),
    path('registerteacher/', views.register_teacher, name='register-teacher'),

    path('login/', views.Login_user, name='login'),
    path('signup/', views.sign_up, name='sign-up'),
    path('logout/', views.Logout_user, name='logout'),

    path('delete-student/<str:pk>/', views.delete_student, name='delete-student'),
    path('edit-student/<str:pk>/', views.edit_student, name='edit-student'),
]
