from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from .forms import AnimalForm,BirdForm,CustomerForm,DoctorForm,AppoinmentForm
from.models import Animal,Bird,Customer,Doctor,Appoinment

# pets/views.py

from django.shortcuts import render, redirect
from .models import AdminLogin

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()  # Remove leading/trailing spaces

        try:
            admin = AdminLogin.objects.get(username=username)

            # Debugging: Print both entered and stored passwords
            print(f"Entered Password: '{password}'")
            print(f"Stored Password: '{admin.password}'")

            # Check if the passwords match
            if admin.password == password:
                return redirect('admin_dashboard')  # Change to your actual admin dashboard URL
            else:
                error = "Incorrect password"
                print("Password mismatch")
        except AdminLogin.DoesNotExist:
            error = "Admin username not found"
            print("Username not found")
        
        return render(request, 'admin_login.html', {'error': error})

    return render(request, 'admin_login.html')

# Index view (Homepage)
def index(request):
    return render(request, 'index.html')

# User login view (function-based)
def user_dashboard(request):
    # You can add logic to fetch user-specific data or other content for the dashboard
    return render(request, 'user_dashboard.html') 


      
def admin_dashboard(request):
    # Add logic for the dashboard page, like fetching data, etc.
    return render(request, 'admin_dashboard.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AnimalForm
from .models import Animal

def add_animal(request):
    # Generate next Pet ID
    last_pet = Animal.objects.order_by('pet_id').last()
    if last_pet:
        last_id = last_pet.pet_id
        numeric_part = int(last_id[3:])  # remove 'PET'
        new_pet_id = f"PET{numeric_part + 1:03}"  # PET001, PET002, ...
    else:
        new_pet_id = "PET001"

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.pet_id = new_pet_id  # Assign generated ID
            animal.save()
            messages.success(request, f"Animal added successfully! ID: {animal.pet_id}")
            return redirect('add_animal')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = AnimalForm(initial={'pet_id': new_pet_id})

    return render(request, 'add_animal.html', {'form': form})



def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})
def edit_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)

        if form.is_valid():
            updated_animal = form.save(commit=False)
            updated_animal.pet_id = animal.pet_id  # Keep Pet ID unchanged
            updated_animal.save()
            messages.success(request, f"Animal {animal.pet_id} updated successfully!")
            return redirect('animal_list')  # Redirect to animal list
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AnimalForm(instance=animal)

    return render(request,'edit_animal.html', {'form': form, 'animal': animal})


# Delete Animal
def delete_animal(request, pk):
    if request.method == 'POST':
        animal = get_object_or_404(Animal, pk=pk)
        animal.delete()
        messages.success(request, f"Animal {animal.pet_id} deleted successfully!")
        return redirect('animal_list')  # Redirect to animal list

    messages.error(request, 'Invalid request method.')
    return redirect('animal_list')

def add_bird(request):
    # Generate next Pet ID
    last_pet = Bird.objects.order_by('bird_id').last()
    if last_pet:
        last_id = last_pet.bird_id
        numeric_part = int(last_id[3:])  # remove 'PET'
        new_pet_id = f"BRD{numeric_part + 1:03}"  # PET001, PET002, ...
    else:
        new_pet_id = "BRD001"

    if request.method == 'POST':
        form = BirdForm(request.POST)
        if form.is_valid():
            bird = form.save(commit=False)
            bird.bird_id = new_pet_id  # Assign generated ID
            bird.save()
            messages.success(request, f"bird added successfully! ID: {bird.bird_id}")
            return redirect('add_bird')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = BirdForm(initial={'bird_id': new_pet_id})

    return render(request, 'add_bird.html', {'form': form})



def bird_list(request):
    birds = Bird.objects.all()
    return render(request, 'bird_list.html', {'birds': birds})

def edit_bird(request, pk):
    bird = get_object_or_404(Bird, pk=pk)

    if request.method == 'POST':
        form = BirdForm(request.POST, instance=bird)

        if form.is_valid():
            updated_bird = form.save(commit=False)
            updated_bird.bird_id = bird.bird_id  # Keep Pet ID unchanged
            updated_bird.save()
            messages.success(request, f"bird {bird.bird_id} updated successfully!")
            return redirect('bird_list')  # Redirect to animal list
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BirdForm(instance=bird)

    return render(request,'edit_bird.html', {'form': form, 'animal': bird})


# Delete Animal
def delete_bird(request, pk):
    if request.method == 'POST':
        bird = get_object_or_404(Bird, pk=pk)
        bird.delete()
        messages.success(request, f"Bird{bird.bird_id} deleted successfully!")
        return redirect('bird_list')  # Redirect to animal list

    messages.error(request, 'Invalid request method.')
    return redirect('bird_list')

def add_customer(request):
    # Generate next Pet ID
    last_pet = Customer.objects.order_by('cust_id').last()
    if last_pet:
        last_id = last_pet.cust_id
        numeric_part = int(last_id[3:])  # remove 'PET'
        new_pet_id = f"CUS{numeric_part + 1:03}"  # PET001, PET002, ...
    else:
        new_pet_id = "CUS001"

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer  = form.save(commit=False)
            customer .cust_id = new_pet_id  # Assign generated ID
            customer .save()
            messages.success(request, f"customer  added successfully! ID: {customer.cust_id}")
            return redirect('add_customer')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = CustomerForm(initial={'cust_id': new_pet_id})

    return render(request, 'add_customer.html', {'form': form})



def customer_list(request):
    customers  = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def edit_customer(request, pk):
    customer  = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            updated_bird = form.save(commit=False)
            updated_bird.cust_id = customer.cust_id  # Keep Pet ID unchanged
            updated_bird.save()
            messages.success(request, f"customer {customer.cust_id} updated successfully!")
            return redirect('customer_list')  # Redirect to animal list
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerForm(instance=customer)

    return render(request,'edit_customer.html', {'form': form, 'customer': customer})


# Delete Animal
def delete_customer(request, pk):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        messages.success(request, f"customer {customer.cust_id} deleted successfully!")
        return redirect('customer_list')  # Redirect to animal list

    messages.error(request, 'Invalid request method.')
    return redirect('customer_list')

def add_doctor(request):
    # Generate next Pet ID
    last_pet = Doctor.objects.order_by('doct_id').last()
    if last_pet:
        last_id = last_pet.doct_id
        numeric_part = int(last_id[3:])  # remove 'PET'
        new_pet_id = f"DOT{numeric_part + 1:03}"  # PET001, PET002, ...
    else:
        new_pet_id = "DOT001"

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor  = form.save(commit=False)
            doctor.doct_id = new_pet_id  # Assign generated ID
            doctor.save()
            messages.success(request, f"doctor added successfully! ID: {doctor.doct_id}")
            return redirect('add_doctor')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = DoctorForm(initial={'doct_id': new_pet_id})

    return render(request, 'add_doctor.html', {'form': form})



def doctor_list(request):
    doctors  = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def edit_doctor(request, pk):
    doctor  = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            updated_bird = form.save(commit=False)
            updated_bird.doct_id = doctor.doct_id  # Keep Pet ID unchanged
            updated_bird.save()
            messages.success(request, f"customer {doctor.doct_id} updated successfully!")
            return redirect('doctor_list')  # Redirect to animal list
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DoctorForm(instance=doctor)

    return render(request,'edit_doctor.html', {'form': form, 'doctor': doctor})


# Delete Animal
def delete_doctor(request, pk):
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        messages.success(request, f"doctor {doctor.doct_id} deleted successfully!")
        return redirect('doctor_list')  # Redirect to animal list

    messages.error(request, 'Invalid request method.')
    return redirect('doctor_list')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'user_login.html')

        # Authenticate from Customer table
        user = Customer.objects.filter(username=username, password=password).first()

        if user:
            request.session['customer_id'] = user.cust_id
            request.session['customer_name'] = user.name
            messages.success(request, 'Login Successful!')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user_login.html')




def add_Appoinment(request):
    if request.method == 'POST':
        form = AppoinmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment registered successfully!')
            return redirect('add_appoinment')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Generate new Appointment ID
        last_appoinment = Appoinment.objects.order_by('APT_id').last()
        if last_appoinment:
            last_id = last_appoinment.APT_id
            numeric_part = int(last_id[3:])
            new_appoinment_id = f"APT{numeric_part + 1:03}"
        else:
            new_appoinment_id = "APT001"

        form = AppoinmentForm(initial={'APT_id': new_appoinment_id})

    return render(request, 'add_appoinment.html', {'form': form})

def get_doctor_details(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        data = {
            'hospital': doctor.hospital,
            'place': doctor.place,
        }
    except Doctor.DoesNotExist:
        data = {'hospital': '', 'place': ''}
    return JsonResponse(data)


def view_appoinments(request):
    views=Appoinment.objects.all()
    return render(request,'view_appointments.html',{'views':views})

def admin_view_appoinments(request):
    
    views=Appoinment.objects.all()
    return render(request,'admin_view_appoinment.html',{'views':views})




