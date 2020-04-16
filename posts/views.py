from django.shortcuts import render
#from django.http import HttpResponse

from .models import Post

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

#def index(request):
    # одна строка вместо тысячи слов на SQL
#    latest = Post.objects.order_by('-pub_date')[:10]
    # собираем тексты постов в один, разделяя новой строкой
#    output = []
#    for item in latest:
#        output.append(item.text)
#    return HttpResponse('\n'.join(output))