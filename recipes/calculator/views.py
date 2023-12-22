from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }}
   
def cook(request, recipe_name):
    if recipe_name in DATA.keys():
        servings = request.GET.get('servings', 1)
        data = {}
        for ingredient in DATA[recipe_name]:
            data[ingredient] = round(DATA[recipe_name][ingredient] * int(servings), 2)
        context = {
            'recipe': data
        }
    else:
        context = {}
    return render(request, 'calculator/dishes.html', context)

def home_view(request):
    dishes_list = [dishes for dishes in DATA.keys()]
    context ={"dishes_list":dishes_list}
    return render(request, "calculator/home_view.html", context)
    
    
