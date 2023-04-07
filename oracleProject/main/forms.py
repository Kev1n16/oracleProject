from django.forms import ModelForm
from main.models import Flavor

from .models import User
from .models import User
class UserInformation(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        labels = {
            'username': "Username",
            'password': "Password",
            'remember': "Remember login"
        }


class FlavorInputForm(ModelForm):
    class Meta:
        model = Flavor
        fields = ('__all__')

