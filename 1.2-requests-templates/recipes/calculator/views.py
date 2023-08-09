from django.shortcuts import render, reverse

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
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def main(request):

    pages = {
        'Главная страница': reverse('home'),
        'Омлет': 'omlet',
        'Паста': 'pasta',
        'Бутер': 'buter'
    }

    context = {
        'pages': pages
    }
    return render(request, 'calculator/main.html', context)


def dish_view(request, dish):

    data = DATA
    servings = int(request.GET.get('servings', 1))
    for ingr, count in DATA[dish].items():
        data[dish][ingr] = count*servings

    context = {
        'recipe': data[dish]
    }

    return render(request, 'calculator/index.html', context)
