from djando import forms
from basic_app.models import UserProfileInfo

class UserForm(models.ModelForm):

       password = forms.CharField(widget = forms.PasswordInput())

       class Meta():
           model = User
           fields = ('username','password','email')
    

class UserProfileInfoForm(models.ModelForm):
  
        class Meta():
 
            model = UserProfileInfoForm
            fields = ('profile_pic','portfolio_site')
