# pets/forms.py
from django import forms
from .models import Animal,Bird,Customer,Doctor,Appoinment

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['pet_id', 'category', 'breed', 'weight', 'height', 'age', 'fur_type', 'cost']

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['bird_id', 'category', 'type', 'cost', 'noice_level']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_id', 'name', 'username', 'phone', 'address','password']

        widgets={
            'password':forms.PasswordInput
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doct_id', 'doct_name', 'category', 'hospital', 'place']

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = ['APT_id', 'pet_name', 'date', 'time', 'doctor','hospital_name','place','other_query']

        widgets = {
            'hospital_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'place': forms.TextInput(attrs={'readonly': 'readonly'}),

            'date': forms.DateInput(attrs={'type': 'date',}),
            'time': forms.TimeInput(attrs={'type': 'time',}),
        }


        

      



 
