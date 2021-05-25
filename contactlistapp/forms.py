from django import forms
from .models import Mycontact

class Contactform(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
        #super(Contactform, self).__init__(*args, **kwargs)
        #self.fields['Contactform_text'].widget.attrs['placeholder'] = self.instance.placeholder

    class Meta:
        model = Mycontact
        fields = '__all__'


        #widgets = {'__all__': forms.TextInput(attrs={'placeholder': ''})}