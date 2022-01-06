from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, Attendanceform
from core.models import Attendance, Profile
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime 
import csv

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(data=request.POST)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit = False)
            profile.user = user
            profile.save()
            
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        content = {
            'u_form' : UserRegisterForm(),
            'p_form' : ProfileUpdateForm(),
            "title" : "Register"
        }
        return render(
                    request, 
                    'accounts/register.html', 
                    content
                )
    
    return redirect('home')

@staff_member_required(login_url='login')
def profile_list(request):
    users = User.objects.all()
    l = []
    for user in users:
        l.append([user.username, user.id])
    return render(request, 'accounts/profilelist.html', {'userlist' : l})    
    

@staff_member_required(login_url='login')
def profile(request, user_id=0):
    if request.method == 'POST':
        user = User.objects.filter(id=user_id)[0]
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')
        return redirect('home')
    else:
        user = User.objects.filter(id=user_id)[0]
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'head_title' : request.user.username
    }

    return render(request, 'accounts/profile.html', context)


def home_view(request):
    content = {"title" : "Home" }
    return render(request, 'index.html', content)


def attendance(request):
    if request.method == "POST":
        a_form = Attendanceform(request.POST)
        attend = a_form.save(commit=False)
        
        if 'roll_number' in request.POST:
            profile = Profile.objects.filter(roll_number=request.POST['roll_number'])[0]
            if not profile:
                messages.error(request, f"Rollnumber couldn't found")
                return redirect('attendance')
            if Attendance.objects.filter(date=datetime.today(), profile_id=profile.id) :
                messages.error(request, f"Already attendance added")
                return redirect('attendance')
            
            attend.profile = profile
            attend.save()
            
        if a_form.is_valid():
            a_form.save()
            messages.success(request, f'Succufully added Attendance!')
            return redirect('attendance')
        return redirect('attendance')
    else:
        a_form = Attendanceform()
        content = {
            'form' : a_form
        }
        return render(request, 'accounts/attendance.html', content)        
            
        
    
def attendanceListToday(request):
    users = Attendance.objects.filter(
                        date=datetime.today(), 
                        attendance='present'
                    )
    content = {'users' : users}    
    
    return render(request, 'accounts/attendanceListToday.html', content )

def get_attendance_sheet(request):
    response = HttpResponse(content_type='text/csv')  
    file_name = 'attendance-list-{}.csv'.format(datetime.today().strftime("%d-%b-%Y"))
    print(file_name)
    response['Content-Disposition'] = 'attachment; filename={}'.format(file_name) 
    writer = csv.writer(response)
    writer.writerow(["username","Roll Number" ,"Department", "Bus Number", "email", "Fees Paid Status", "Attendance Status"])
    
    users = User.objects.all()

    for user in users:
        profile = Profile.objects.get(user=user)
        try : 
            attendance_status = Attendance.objects.get(profile=profile, date=datetime.today()).attendance
        except ObjectDoesNotExist:
            attendance_status = 'absent'
        writer.writerow([user.username, 
                         profile.roll_number, 
                         profile.department, 
                         profile.bus_number, 
                         user.email, 
                         "Paid" if profile.is_fees_paid else "Not Paid",
                         attendance_status
                         ])  
        
    return response  