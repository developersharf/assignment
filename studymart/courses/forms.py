from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#  when we have important data in our form, then, we use: 
#  GET method(it shows data in the SearchBar, even passwords), otherwise, 
#  we use POST(it hides the data, doesn't put them in SearchBar)
#  GET method is faster than POST method



class StudentRegistration(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Please enter you first name'})
    last_name = forms.CharField(error_messages={'required':'Please enter you last name'})
    email = forms.EmailField(required=False)
    batch = forms.IntegerField(help_text='Enter your batch number', min_value=1)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=12)
    re_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=12)
    textarea = forms.CharField(widget=forms.Textarea())
    
    # mentor's code
    # ----------------- 
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password_match = self.cleaned_data['password']
    #     re_password_match = self.cleaned_data['re_password']
        
    #     if password_match != re_password_match:
    #         raise forms.ValidationError("Password doesn't match")
    
    
    
    # refined
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match")



#User creation forms 'customized'

class usercform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', ]