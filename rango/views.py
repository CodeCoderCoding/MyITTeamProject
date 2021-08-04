from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import City, Scenery
from rango.forms import UserLikedCityForm, UserForm, UserProfileForm
from datetime import datetime


def home(request):
    city_list = City.objects.order_by('-likes')[:5]
    scenery_list = Scenery.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['cities'] = city_list
    context_dict['sceneries'] = scenery_list

    visitor_cookie_handler(request)

    return render(request, 'rango/home.html', context=context_dict)


def about(request):
    # Spoiler: now you DO need a context dictionary!
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)


def show_scenery(request, city_name_slug):
    context_dict = {}

    try:
        city = City.objects.get(slug=city_name_slug)
        sceneries = Scenery.objects.filter(city=city)

        context_dict['sceneries'] = sceneries
        context_dict['city'] = city
    except City.DoesNotExist:
        context_dict['sceneries'] = None
        context_dict['city'] = None

    return render(request, 'rango/scenery.html', context=context_dict)


@login_required
def add_city(request, user_name_slug):
    form = UserLikedCityForm()

    if request.method == 'POST':
        form = UserLikedCityForm(request.POST)

        if form.is_valid():
            city = form.save(commit=False)
            city.user = user_name_slug
            city.save()

            return redirect(reverse('rango:home'))
        else:
            print(form.errors)

    context_dict = {'form': form, 'username': user_name_slug}

    return render(request, 'rango/add_city.html', context=context_dict)


@login_required
def add_scenery(request, city_name_slug):
    try:
        city = City.objects.get(slug=city_name_slug)
    except:
        city = None

    # You cannot add a scenery to a Category that does not exist... DM
    if city is None:
        return redirect(reverse('rango:home'))

    form = SceneryForm()

    if request.method == 'POST':
        form = SceneryForm(request.POST)

        if form.is_valid():
            if city:
                scenery = form.save(commit=False)
                scenery.city = city
                scenery.views = 0
                scenery.save()

                return redirect(reverse('rango:show_scenery', kwargs={'city_name_slug': city_name_slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.

    context_dict = {'form': form, 'city': city}
    return render(request, 'rango/add_scenery.html', context=context_dict)


@login_required
def mypage(request):
    return render(request, 'rango/mypage.html')


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits