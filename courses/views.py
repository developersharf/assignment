from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import path
from . models import Student, Info
from . forms import StudentRegistration, usercform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def courses(request):
    course1 = 'Python'
    course2 = 'Java'    
    course3 = 'C++'
    course4 = 'JavaScript'
    course5 = 'HTML'
    course6 = 'CSS'

    freeCourse_details = {'c1': course1, 'c2': course2, 'c3': course3, 'c4': course4, 'c5': course5, 'c6': course6}
    
    return render(request, 'courses/courses.html', freeCourse_details)


def free(request):
    fcrs = 10  
    return render(request, 'courses/freecourses.html', {'fcrs': fcrs})


    # return HttpResponse("<h1>Python</h1>")
    
def paid(request):
    return render(request, 'courses/paid.html')



def investor(request):
    sdetails = Student.objects.all()
    return render(request, 'courses/investor.html', {'std': sdetails})

def show_form(request):
    
    if request.method == 'POST':
        
        frm = StudentRegistration(request.POST)
        if frm.is_valid():
            fname = frm.cleaned_data['first_name']
            lname = frm.cleaned_data['last_name']
            eml = frm.cleaned_data['email']
            btc = frm.cleaned_data['batch']
            pswd = frm.cleaned_data['password']
            repswd = frm.cleaned_data['re_password']
            txt = frm.cleaned_data['textarea']
            djangoten = Info(first_name = fname, last_name = lname, email = eml, batch = btc, password = pswd, re_password = repswd, textarea = txt)
            djangoten.save()
            return redirect('success')
            
    else:
        
        frm = StudentRegistration()
        print('Execute Get Method')
        
    # frm = StudentRegistration(auto_id=False)
    # frm = StudentRegistration(auto_id=True, label_suffix=' -> ', initial={'email': 'sharfarsalan@gmail.com'})
    # frm.order_fields(field_order=['last_name', 'first_name', 'batch', 'email'])
    return render(request, 'courses/forms.html', {'form': frm}) 


def success(request):
    return render(request, 'courses/submit.html') 


def usercfrom(request):
    if request.method == 'POST':
        form = usercform(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = usercform()
    return render(request, 'courses/userform.html', {'frm': form})



def loginform(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'frm': form})