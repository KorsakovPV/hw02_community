from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Group

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

#Создать view-функцию group_posts
def group_posts(request, slug):
    #return HttpResponse(slug)
    # функция get_object_or_404 получает по заданным критериям объект из базы данных 
    # или возвращант сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)
    #return HttpResponse(group)
    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    #return HttpResponse(posts[0][0])
    return render(request, "group.html", {"group": group, "posts": posts})
