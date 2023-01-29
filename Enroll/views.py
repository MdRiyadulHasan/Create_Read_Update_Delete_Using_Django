from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# This function will add a new item and show all the data
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            ph = fm.cleaned_data['phone']
            reg = User(name=nm, email =em, password=ps, phone=ph)
            reg.save()
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
    stud = User.objects.all()
    
    return render(request,'Enroll/addandshow.html', {'form':fm, 'stu':stud})
# update data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'Enroll/update.html', {'form':fm})

# delete function
def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
