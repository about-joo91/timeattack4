from django.shortcuts import render
from .models import Drink, Category, ImageModel

# Create your views here.


def home(request):
    return render(request, 'base.html')

def product(request):
    cold_brew = request.POST.get('cold_brew')
    brewed = request.POST.get('brewed')
    espresso = request.POST.get('espresso')
    check = {
        'cold_brew': '콜드 브루 커피',
        'brewed' : '브루드 커피',
        'espresso' : '에스프레소'
    }
    cate_name = cold_brew or brewed or espresso
    category = Category.objects.get(name = check[cate_name])
    drinks = Drink.objects.filter(category= category)
    # drink_list = []
    # for drink in drinks:
    #     img_url = ImageModel.objects.get(drink= drink)
    #     drink_list.append({
    #         'drink' : drink.name,
    #         'img' : img_url
    #     })

    return render(request,'products.html', {'drinks' : drinks})
        
