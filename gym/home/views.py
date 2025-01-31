from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Registration
from django.contrib import messages

# Create your views here.

def index(request):
    # messages.success(request, "This is test message")
    
    return render(request, 'index.html')

def exercises(request):
    return render(request, 'exercises.html')

def chest(request):
    return render(request, 'chest.html')

def back(request):
    return render(request, 'back.html')

def bicep(request):
    return render(request, 'bicep.html')

def tricep(request):
    return render(request, 'tricep.html')

def shoulder(request):
    return render(request, 'shoulder.html')

def legs(request):
    return render(request, 'legs.html')

def abs(request):
    return render(request, 'abs.html')

def membership(request):
    return render(request, 'membership.html')

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        phone = request.POST.get('phone')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        fitnessGoal = request.POST.get('fitnessGoal')
        
        registration = Registration(name=name, email=email, occupation =occupation, phone= phone, weight= weight, height = height, fitnessGoal = fitnessGoal, date = datetime.today() )
        registration.save() 
        messages.success(request, "Your data has been stored successfully. Our team will contact you through Email for further details.")
        # messages.success(request, "")
    
    return render(request, 'registration.html')

def chest1(request):
    return render(request, 'chest1.html')

def chest2(request):
    return render(request, 'chest2.html')

def chest3(request):
    return render(request, 'chest3.html')

def chest4(request):
    return render(request, 'chest4.html')

def chest5(request):
    return render(request, 'chest5.html')

def chest6(request):
    return render(request, 'chest6.html')

def chest7(request):
    return render(request, 'chest7.html')

def chest8(request):
    return render(request, 'chest8.html')

def chest9(request):
    return render(request, 'chest9.html')

def chest10(request):
    return render(request, 'chest10.html')