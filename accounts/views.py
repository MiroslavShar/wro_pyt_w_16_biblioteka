from django.shortcuts import render, redirect

from polka.models import Person


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'loginform.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Person.objects.get(username=username, password=password)
        except (Person.DoesNotExist, Person.MultipleObjectsReturned):
            return redirect("/login/")
        request.session['user'] = user