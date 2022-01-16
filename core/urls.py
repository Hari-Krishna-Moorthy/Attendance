from django.urls import path, include

from core.views import (
    register,
    profile_list, 
    profile, 
    home_view, 
    attendance,
    attendanceListToday, 
    attendance_update,
    get_attendance_sheet,
    aboutus,
    attendance_rfid
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('profile/', profile_list, name='profilelist'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('attendance/', attendance, name='attendance'),
    path('attendance/rfid/', attendance_rfid, name='attendance-rfid'),
    path('attendance-today/', attendanceListToday, name='attendance-today'),
    path('attendance-update/', attendance_update, name='attendance-update'),
    path('get-attendance-sheet', get_attendance_sheet, name='get-attendance-sheet'),
    path('aboutus', aboutus, name='aboutus'),    
]

