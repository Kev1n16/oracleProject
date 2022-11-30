from django.forms import ModelForm
from main.models import Flavor


class FlavorInputForm(ModelForm):
    class Meta:
        model = Flavor
        fields = ('name', 'id', 'amt_vCPU', 'amt_Memory',
                  'amt_Volume', 'amt_Ephemeral_Volume')
        labels = {
            'name': "Flavor Name",
            'id': "Flavor ID",
            'amt_vCPU': "Amount of vCPUs",
            'amt_Memory': "Amount of Memory (GB)",
            'amt_Volume': "Amount of Storage Volume (GB)",
            'amt_Ephemeral_Volume': "Amount of Ephemeral Storage Volume (GB)"
        }
