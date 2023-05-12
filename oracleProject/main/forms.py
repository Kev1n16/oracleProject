from django.forms import ModelForm
from main.models import *

# form for the secondary user account data base
class UserInformation(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        labels = {
            'username': "Username",
            'password': "Password",
            'remember': "Remember login"
        }


# form for all of the flavor values
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

# Adaptor form for dataset
class PredictInputForm(ModelForm):
    class Meta:
        model = Predict
        fields = ('amt_CPU', 'amt_vCPU', 'prcnt_CPU', 'amt_Memory',
                  'used_Memory')

        labels = {
            'amt_CPU': "CPU Cores",
            'amt_vCPU': "vCPU (MHz)",
            'prcnt_CPU': "Average Percent CPU Usage",
            'amt_Memory': "Memory (KB)",
            'used_Memory': "Average Percent Memory Usage"
        }
