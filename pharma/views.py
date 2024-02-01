from django.shortcuts import render, get_object_or_404, redirect
from .models import Dealer, Medicine, Employee, Customer, Purchase
from .forms import DealerForm, MedicineForm, EmployeeForm, CustomerForm, PurchaseForm



def edit_dealer(request, pk):
    dealer = get_object_or_404(Dealer, pk=pk)
    
    if request.method == 'POST':
        form = DealerForm(request.POST, instance=dealer)
        if form.is_valid():
            form.save()
            return redirect('dealertable')
    else:
        form = DealerForm(instance=dealer)

    return render(request, 'pages/dealer_edit.html', {'form': form, 'dealer': dealer})

def delete_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)

    if request.method == 'POST':
        dealer.delete()
        return redirect('dealertable')

    return render(request, 'pages/dealer_confirm_delete.html', {'dealer': dealer})

def home(request):
    return render(request, 'pages/homepage.html')

def dealertable(request):
    dealers = Dealer.objects.all()
    context = {'dealers': dealers}
    return render(request, 'pages/dealertable.html', context)

def medtable(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'pages/medtable.html', context)

def emptable(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'pages/emptable.html', context)

def dealerforminsert(request):
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dealertable")
    else:
        form = DealerForm()

    context = {'form': form}
    return render(request, "pages/dealeradd.html", context)

def medAdd(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("medtable")
    else:
        form = MedicineForm()

    context = {'form': form}
    return render(request, "pages/medAdd.html", context)

def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medtable')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'pages/medicine_edit.html', {'form': form, 'medicine': medicine})

def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, medicine_id=medicine_id)

    if request.method == 'POST':
        medicine.delete()
        return redirect('medtable')

    return render(request, 'pages/medicine_confirm_delete.html', {'medicine': medicine})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emptable')
    else:
        form = EmployeeForm()

    return render(request, 'pages/add_employee.html', {'form': form})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('emptable')

    return render(request, 'pages/delete_employee.html', {'employee': employee})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emptable')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'pages/edit_employee.html', {'employee': employee, 'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'pages/customer_table.html', {'customers': customers})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'pages/edit_customer.html', {'form': form, 'customer': customer})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'pages/delete_customer.html', {'customer': customer})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Replace with your actual URL name for the customer table
    else:
        form = CustomerForm()

    return render(request, 'pages/add_customer.html', {'form': form})

def purchase_table(request):
    purchases = Purchase.objects.all()
    context = {'purchases': purchases}
    return render(request, 'pages/purchase_table.html', context)

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_table')
    else:
        form = PurchaseForm()

    return render(request, 'pages/add_purchase.html', {'form': form})

def edit_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase_table')
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'pages/edit_purchase.html', {'form': form, 'purchase': purchase})

def delete_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase_table')

    return render(request, 'pages/delete_purchase.html', {'purchase': purchase})