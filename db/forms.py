from .models import *
from django.forms import ModelForm

class AccountsForm(ModelForm):
    class Meta:
        model = Accounts
        fields=['name','password','phoneno']
class Roomform(ModelForm):
    class Meta:
        model=Room
        fields=['roomid','roomname']

class Memberform(ModelForm):
    class Meta:
        model=Member
        fields=['phoneno','nameofmem']
        
class Messageform(ModelForm):
    class Meta:
        model=Message
        fields=['msgfrom','text']