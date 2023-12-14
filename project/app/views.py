from django.shortcuts import render, redirect
from .models import UserModel,Order
from datetime import datetime
from .forms import AddMen

def index(request):
    # age = request.POST.get('age')
    people = UserModel.objects.order_by('-id')
    chel = UserModel.objects.count()
    return render(request,'app/index.html',context={'people':people,'chel':chel})

def order(request):
    createOders()
    orders = Order.objects.filter(datetime__month__gte=6) & Order.objects.filter(datetime__day=23)
    return render(request, 'app/orders.html', context={'orders': orders})

def create(request):
    if request.method == 'POST':
        form = AddMen(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            UserModel.objects.create(name=name,age=age)
            return redirect('home')

    form = AddMen()
    return render(request,'app/create.html',context={'form':form})

def update(request,id):
    try:
        men = UserModel.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.age = request.POST.get('age')
            men.save()
            return redirect('home')
        else:
            return render(request,'app/update.html',context={'men': men})
    except:
        return redirect('create')

def delete(request,id):
    try:
        men = UserModel.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('home')

def user(request,id):
    try:
        men = UserModel.objects.get(id=id)
        return render(request, 'app/user.html', context={'men': men})
    except:
        return redirect('home')
def createOders():
    if Order.objects.count()< 5:
        Order.objects.create(datetime=datetime(2020,6,23,1,23,52))
        Order.objects.create(datetime=datetime(2023, 8, 22, 2, 46, 52))
        Order.objects.create(datetime=datetime(2022, 2, 14, 20, 52, 52))
        Order.objects.create(datetime=datetime(2024, 3, 6, 6, 20, 52))
        Order.objects.create(datetime=datetime(2013, 9, 3, 12, 15, 52))
