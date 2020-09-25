from django.shortcuts import render
from herotest.models import HeroInfo
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


# Create your views here.
def index(request):
    heros = HeroInfo.objects.all()
    return render(request, 'herotest/index.html', {'heros': heros})


def add_check(request):
    hero = HeroInfo()
    heroname = request.POST.get('heroname')
    herogender = request.POST.get('herogender')
    heroskill = request.POST.get('heroskill')
    hero.name = heroname
    hero.skill = heroskill
    if herogender == 'male' or herogender == '男':
        hero.gender = True
    elif herogender == 'female' or herogender == '女':
        hero.gender = False
    else:
        return HttpResponse('Incorrect input!')
    hero.save()
    # return render(request, 'herotest/index.html')
    return HttpResponseRedirect('/index')


def add_ajax_check(request):
    hero = HeroInfo()
    heroname = request.POST.get('name')
    herogender = request.POST.get('gender')
    heroskill = request.POST.get('skill')
    hero.name = heroname
    hero.skill = heroskill
    if herogender == 'male' or herogender == 'Male' or herogender == 'MALE' or herogender == '男':
        hero.gender = True
    elif herogender == 'female' or herogender == 'Female' or herogender == 'FEMALE' or herogender == '女':
        hero.gender = False
    else:
        return JsonResponse({'res': 0})
        # return HttpResponse('Incorrect input!')
    hero.save()
    # return render(request, 'herotest/index.html')
    # return HttpResponseRedirect('/index')
    return JsonResponse({'res': 1})


def add_return(request):
    return JsonResponse({'res': 1})


def delete(request, id):
    hero = HeroInfo.objects.get(id=id)
    hero.delete()
    return HttpResponseRedirect('/index')


def add(request):
    print("jiayou")
    return render(request, 'herotest/add.html')


def addhero(request):
    hero = HeroInfo()
    hero.name = 'one'
    hero.gender = False
    hero.skill = 'two'
    hero.save()
    return HttpResponseRedirect('/index')


def update(request, id):
    hero1 = HeroInfo.objects.get(id=id)
    hero = hero1
    if hero.gender:
        hero.gender = 'Male'
    else:
        hero.gender = 'Female'
    return render(request, 'herotest/update.html', {'hero': hero})


def update_check(request, id):
    hero = HeroInfo.objects.get(id=id)
    heroname = request.POST.get('heroname')
    herogender = request.POST.get('herogender')
    heroskill = request.POST.get('heroskill')
    hero.name = heroname
    hero.skill = heroskill
    if herogender == 'male' or herogender == 'Male' or herogender == 'MALE' or herogender == '男':
        hero.gender = True
    elif herogender == 'female' or herogender == 'Female' or herogender == 'FEMALE' or herogender == '女':
        hero.gender = False
    else:
        return HttpResponse('Incorrect input!')
    hero.save()
    # return render(request, 'herotest/index.html')
    return HttpResponseRedirect('/index')
