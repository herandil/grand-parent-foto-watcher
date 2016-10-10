from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.views import auth_check
from django.template import Context
from slider.forms import SliderForm
from database.models import Slides, Background, User
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    if not auth_check(request):
        return HttpResponseRedirect("/login/")
    user = User.objects.get(id=request.session['user_id'])
    sliders = Slides.objects.filter(user=user)
    c = Context({'sliders': sliders})
    return render(request, 'slider_home/index.html', c)


def detail(request, slider_id):
    if not auth_check(request):
        return HttpResponseRedirect("/login/")
    # print slider_id
    if request.method == 'GET':
        if slider_id and slider_id != "":
            try:
                user_id = request.session['user_id']
                # slider = Slides.objects.get(id=slider_id)
                user = User.objects.get(id=user_id)
                slider = Slides.objects.filter(user=user).get(id=slider_id)
                c = Context({"slider": slider})
                return render(request, 'slider_detail/index.html', c)
            except ObjectDoesNotExist:
                print "error"
                return HttpResponseRedirect('/error/')

    return HttpResponseRedirect('/error/')


def create_page(request):
    if not auth_check(request):
        return HttpResponseRedirect("/login/")
    c = Context({
        "form": SliderForm
    })

    return render(request, "slider_create/index.html", c)


def create(request):
    if not auth_check(request):
        return HttpResponseRedirect("/login/")
    if request.method == 'POST':
        form = SliderForm(request.POST)

        if form.is_valid():
            # make new slider
            slider = Slides()
            slider.title = form.cleaned_data['title']
            slider.desc = form.cleaned_data['desc']
            slider.speed = form.cleaned_data['speed']
            slider.background = Background.objects.get(id=1)
            slider.save()
            # Set the many to many relation
            user = User.objects.get(id=request.session['user_id'])
            slider.user.add(user)

            return HttpResponseRedirect('/thanks/')

    return HttpResponseRedirect('/error/')


