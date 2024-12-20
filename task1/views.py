from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from .models import Game, Buyer


def product_list(request):
    games = Game.objects.all()
    # Передаем коллекцию в context
    return render(request, 'shop.html', {'games': games})


def sign_up_by_django(request):
    form = UserRegister()
    info = {'form': form}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(name=username, age=age)
                return redirect('home')
    else:

        UserRegister()

    return render(request, 'registration_page.html', info)


def home(request):
    return render(request, 'home.html')

def shop_view(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
    return render(request, 'shop.html', context)

def cart_view(request):
    return render(request, 'cart.html')

