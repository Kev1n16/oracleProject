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
        fields = ('name', 'id', 'amt_vCPU', 'amt_Memory',
                  'amt_Volume', 'amt_Ephemeral_Volume', 'acctUsername')

        labels = {
            'name': "Flavor Name",
            'id': "Flavor ID",
            'amt_vCPU': "Amount of vCPUs",
            'amt_Memory': "Amount of Memory (GB)",
            'amt_Volume': "Amount of Storage Volume (GB)",
            'amt_Ephemeral_Volume': "Amount of Ephemeral Storage Volume (GB)",
            'Unique ID': "Username"
        }
