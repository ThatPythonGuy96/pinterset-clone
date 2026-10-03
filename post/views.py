from django.shortcuts import render
from .models import Pin, Tag, Board

def index(request):
    pins = Pin.objects.all().order_by('-created')
    tags = Tag.objects.filter(post_tag__isnull=False).distinct()[:4]
    other_tags = Tag.objects.filter(post_tag__isnull=False).distinct()[4:]

    context = {
        'pins': pins,
        'tags': tags,
        'other_tags': other_tags
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    pin = Pin.objects.get(pk=pk)
    more = Pin.objects.all()[5:15]
    context = {
        'pin':pin,
        'more': more
    }
    return render(request, 'post.html', context)  

def tag(request, tag):
    tags = Pin.objects.filter(pin_tag=tag).order_by('-created')
    tag = Tag.objects.get(pk=tag)

    context = {
        'tags': tags,
        'tag': tag
    }
    return render(request, 'tag.html', context)

def board(request, name):
    board = Board.objects.filter(name=name)
    context = {
        'board': board
    }
    return render(request, 'board.html', context)