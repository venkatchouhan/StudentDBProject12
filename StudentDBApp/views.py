from django.shortcuts import render
from StudentDBApp.models import Student

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);




from StudentDBApp.models import Student2;
def student_homepage(request):				#new
    students= Student2.objects.all()
    students=Student2.objects.filter(marks__lt=35)
    students=Student2.objects.filter(name__startswith='A')
    students=Student2.objects.all().order_by('marks')  #ASC
    students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentDBApp/index.html', {'students':students})


#form-view(html-form)
from StudentDBApp import forms;
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentDBApp/input.html',context=dict1)



from StudentDBApp import forms;
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentDBApp/input.html',context=dict1)

import time;
from StudentDBApp import forms;
def studentinputverifyview(request):
    if request.method == 'POST':
        formsObj = forms.StudentForm(request.POST);
        if formsObj.is_valid():
            print('Form-Request validation success and printing data');
            time.sleep(5)
            print('Name:', formsObj.cleaned_data['name'])
            print('Marks:', formsObj.cleaned_data['marks'])
            formsObj = forms.StudentForm();     #empty-form
            dict1 = {'form1': formsObj,'msg':'Data Submitted successfully...(Enter another data)'}
    return render(request, 'StudentDBApp/input.html',context=dict1);


import time;
from django.shortcuts import render
from StudentDBApp.forms import StudentForm
#Create your views here>
def studentinputview2(request):
    sentdata=False;
    if request.method=='POST':
        formObj=StudentForm(request.POST)
        if formObj.is_valid():
            print('Form-Request-data Validation Success and printing data')
            time.sleep(5)
            print('Name:',formObj.cleaned_data['name'])
            print('Marks:',formObj.cleaned_data['marks'])
            sentdata=True;
            formObj = StudentForm();            #empty-form
            dict1 = {'form1': formObj, 'sentdata': sentdata}
            return render(request, 'StudentDBApp/thankyou.html', context=dict1);
    formObj=StudentForm();
    dict1={'form1': formObj}
    return render(request,'StudentDBApp/input2.html',context=dict1);