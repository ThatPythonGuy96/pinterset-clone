from django.shortcuts import render
from .models import User
from post.models import Pin, Board

def profile(request, username):
    user = User.objects.get(username=username)
    pictures = Pin.objects.filter(profile=user).order_by('-created')
    boards = Board.objects.filter(profile=username)

    context = {
        'user': user,
        'pictures': pictures,
        'boards': boards
    }
    return render(request, 'author.html', context)