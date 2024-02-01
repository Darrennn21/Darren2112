from django import forms
from .models import Dealer, Medicine ,Employee, Customer, Purchase



class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['name', 'address', 'phone_number', 'email']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_id', 'name', 'dealer', 'description','price', 'stock']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'address', 'email', 'salary', 'phone_number']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer', 'medicine', 'quantity', 'total_price']