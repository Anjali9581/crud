from django.shortcuts import render, redirect # type: ignore
from .models import Operations

def home(request):
    alldetails = Operations.objects.all()
    context = {
        'alldetails': alldetails
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender') == 'True'  # Convert string to boolean

        details = Operations(name=name, email=email, phone=phone, gender=gender)
        details.save()
        return redirect('home')
    return render(request, 'index.html')

def delete(request, id):
    try:
        details = Operations.objects.get(id=id)
        details.delete()
    except Operations.DoesNotExist:
        pass
    return redirect('home')

def edit(request, id):
    try:
        details = Operations.objects.get(id=id)
    except Operations.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender') == 'True'  # Convert string to boolean

        details.name = name
        details.email = email
        details.phone = phone
        details.gender = gender

        details.save()
        return redirect('home')
    else:
        context = {
            'details': details
        }
        return render(request, 'edit.html', context)
