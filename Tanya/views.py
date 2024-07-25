from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from portfolio.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

from .forms import ContactForm
from .models import Home, About, Profile, Category, Portfolio


def index(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }

    return render(request, 'index.html', context)


@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "message from website"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message,
                          "sailor101187@gmail.com",
                          ['sailor101187@gmail.com'],
                          auth_user=EMAIL_HOST_USER,
                          auth_password=EMAIL_HOST_PASSWORD,
                          fail_silently=False,
                          )

            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("index")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
