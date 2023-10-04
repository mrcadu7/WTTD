from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://blogdaengenharia.com/wp-content/uploads/grace-hopper-blog-da-engenharia-4.jpg'},
        {'name': 'Alan Turing', 'photo': 'https://s1.static.brasilescola.uol.com.br/img/2019/09/alan-turing-be.jpg'},
    ]
    return render(request, 'index.html', {'speakers': speakers})
