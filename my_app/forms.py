from django import forms

# defualt django form validation only
class StudentForm1(forms.Form):
    'This will contain defualt validations only!'
    name  = forms.CharField()
    email = forms.EmailField()
    age   = forms.IntegerField()

# custom field level validations
class StudentForm2(forms.Form):
    """In this form we are perform each field level validation one by one using clean_field_name function"""

    name  = forms.CharField()
    email = forms.EmailField()
    age   = forms.IntegerField()
    
    # name validation here
    def clean_name(self):
        """perform name validation here"""
        name = self.cleaned_data['name']
        if(len(name) <4):  # name is less than 4 character
            raise forms.ValidationError('Name must contains 4 characters!')
        
        if( name[0] != ('k' or 'K')): # name must start with K only
            raise forms.ValidationError('Name must start withs K only!')
        
        if (str(name).isalpha() == False ): # number validation here
            raise forms.ValidationError('Name does not contain numbers')

        return name
        
    # email validation here
    def clean_email(self):
        email = self.cleaned_data['email']

        if(len(email) <12):
            raise forms.ValidationError('Email must contain 12 characters!')
            
        return email
            
    # age validation
    def clean_age(self):
        age = self.cleaned_data['age']

        if((age<=10)):
            raise forms.ValidationError('Age must greater than 10')
        if(age>30):
            raise forms.ValidationError('Age must less than 30')
        return age

# complete form validation here
class  StudentForm3(forms.Form):
    """In this form we performing complete form validation using clean function """
    name  = forms.CharField()
    email = forms.EmailField()
    age   = forms.IntegerField()
    
    # complete form validations
    def clean(self):
        """Using different validator to validator form"""
        cleaned_data = super().clean() # calling parent clean method as Form class
        
        # validating name
        if( 'name' in cleaned_data.keys()):
            name = cleaned_data.get('name')
            
            if(len(name)<4):
                raise forms.ValidationError('Name must contains 4 character!')
            
            if(name[0] != ('k' or 'K')):
                raise forms.ValidationError('Name must start with k only')
            
            if((str(name).isalpha()) == False):
                raise forms.ValidationError('Name does not contain numbers')
            
            return name
        
        # validating email
        if('email' in  cleaned_data.keys()):
            email = cleaned_data.get('email')

            if(len(email) <50):
                raise forms.ValidationError('Email must contains 15 characters!')

            
            if((str(email).endswith('.com')) != False):
                raise forms.ValidationError('Email must end with .com')

            
            return email
        
        # validating age here
        if('age' in cleaned_data.keys()):

            age  = cleaned_data.get('age')

            if(age< 17):
                raise forms.ValidationError('Age must be greater than 17')
            
            return age
            



