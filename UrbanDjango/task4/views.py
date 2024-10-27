from django.shortcuts import render

from django.views.generic import TemplateView


class Platform(TemplateView):
    template_name = 'platform.html'


class Cart(TemplateView):
    template_name = 'cart.html'


def menu(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {
        'mydict': mydict,
    }
    return render(request, 'games.html', context)
