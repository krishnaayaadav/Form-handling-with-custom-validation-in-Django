from django.shortcuts import render,redirect
from .forms import StudentForm1,StudentForm2,StudentForm3


# Create your views here.

def defualt_form_validation(request):
    'This is function we  receiving and performing only default validation while student registeration'
    
    
    if request.method =='POST': # handling post request
        form = StudentForm1(request.POST)
        if form.is_valid():
            print('Your form is valid')
            "Now we can perform any operation according to our logic like insertion,delete, updation and many more"
            pass
    else:                       # get request here
        form = StudentForm1() # obj instancetiation  of StudentForm1blank here
    
    context = {
        'val_type': 'Default',
        'form': form
    }
    # this return statement is outline if-else block
    return render(request, 'my_app/registeration_form.html',context) # it function return

# field level validation here
def field_level_validations(request):
    'This is function we  receiving and performing different field level  validation while student registeration'
    # post request hankding 
    if request.method == 'POST':
        form = StudentForm2(request.POST)
        if form.is_valid():
            "fetching here cleaned_data/validated data only"
            stu_name =  form.cleaned_data['name']
            stu_email=  form.cleaned_data['email']
            stu_age  =  form.cleaned_data['age']

            print('Validated data is: ')
            print(stu_name, stu_email, stu_age)
            return redirect('field1') # redirect  here
    else:
        form = StudentForm2()
    context = {
        'form': form,
        'val_type': 'Field Level'


    }
    return render(request, 'my_app/registeration_form.html', context)


def complete_form_validation(request):
    """perform complete form validation here"""
    # post request hankding 
    if request.method =='POST':
        form = StudentForm3(request.POST)
        if form.is_valid(): # fetching valid data from cleaned_data dictionary
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # age   = form.cleaned_data['age']
            print('valid data is: ')
            print('Now can save or perform any other operations')
            # print(name, email, age)
        print('\nSubmitted form is not Valid!\n')
    else: # get request
        form = StudentForm3()
    context = {
        'val_type': 'Complete Form',
        'form': form
    }
    return render(request, 'my_app/registeration_form.html', context)

