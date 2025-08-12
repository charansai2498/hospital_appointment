from django.forms import ModelForm
from app1.models import *
class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'