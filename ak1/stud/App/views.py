
from django.shortcuts import render,redirect
from .forms import studentForm
from django.contrib import messages
from .models import student
def index(request):
    students=student.objects.all()
    return render(request,"index.html",{'students' :students})
def stud_form(request):
    if request.method=='POST':
        form= studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= studentForm()
        return render(request,'form.html',{'form': form })

def remove(request, student_id):
    item = student.objects.get(id=student_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('index')
# Create your views here.
