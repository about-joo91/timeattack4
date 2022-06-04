from django.shortcuts import render
from .models import Drink, Category, ImageModel
import functools
import time
from django.db import connection, reset_queries

# Create your views here.

def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.6f}s")
        return result

    return inner_func
def home(request):
    return render(request, 'base.html')


@query_debugger
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
    drink_list = []
    for drink in drinks:
        img_url = ImageModel.objects.get(drink= drink)
        drink_list.append({
            drink.name : img_url.url
        })
    return render(request,'products.html', {'drink_list' : drink_list})
        
