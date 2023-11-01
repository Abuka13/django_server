from django.urls import reverse
from django.shortcuts import get_object_or_404
from django_app import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django_app.models import PostComments


def home(request):
    return render(request, 'home.html')
@login_required
def list_suggests(request):
    select_orm = models.Suggests.objects.all()
    return render(request, 'list_suggests.html', context={"select_orm": select_orm})
@login_required
def suggest_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "send_suggests.html")
    elif request.method == "POST":

        title = str(request.POST["title"])
        description = str(request.POST["description"])
        date = str(request.POST["date"])
        image = request.FILES["image"]

        models.Suggests.objects.create(
            author=request.user,
            title=title,
            description=description,
            date=date,
            image=image,
            )
        return redirect(list_suggests)

@login_required
def post_detail(request: HttpRequest, pk: str) -> HttpResponse:
    post_obj = models.Suggests.objects.get(id=int(pk))
    post_comments_objs = models.PostComments.objects.all()


    return render(request, "detail.html",{"post": post_obj, "comments": post_comments_objs})

@login_required
def post_comment_create(request: HttpRequest, pk: str) -> HttpResponseRedirect:
    if request.method == "POST":
        post_obj = models.Suggests.objects.get(id=int(pk))
        author = request.user
        text = request.POST.get('text')
        models.PostComments.objects.create(post_id=post_obj.id, author=author, text=text)
        return redirect(reverse('post_detail', args=[pk]))
    else:
        # Возбуждение исключения в случае неправильного метода
        raise Exception("Method not allowed!")





@login_required
def post_delete(request: HttpRequest, pk: str) -> HttpResponseRedirect:
    if request.method == "GET":
        post = models.Suggests.objects.get(id=int(pk))
        post.delete()
        return redirect(list_suggests)
    else:
        raise Exception("Method not allowed!")




@login_required
def vote_comment(request, pk, vote):
    comment = get_object_or_404(PostComments, id=pk)

    if vote == 'up':
        comment.rating += 1
    elif vote == 'down':
        comment.rating -= 1

    comment.save()
    return redirect('post_detail', pk=comment.post.id)











#TODO аутинтефикация
@login_required
def logout_f(request):
    logout(request)
    return redirect(register_f)
def login_f(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #пытается взять имя и пароль из базы данных
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            raise Exception("Данные для входа неправильные!")
    else:
        raise Exception("Method not supported")
def register_f(request):

    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(
            username=username,
            password=make_password(password),
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect(login_f)
    else:
        raise Exception("Method not allowed!")




















