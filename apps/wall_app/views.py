from django.shortcuts import render, redirect
from .models import Message, Comment

# Create your views here.

def index(request):
    context = {
        'messages' : Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all(),
    }
    return render(request, 'wall_app/index.html', context)

def postmessage(request):
    Message.objects.create(name=request.POST['name'], message=request.POST['message'])
    return redirect('/')

def postcomment(request):
    context = {
        'id':request.POST['message_id'],
        'message': Message.objects.get(id=request.POST['message_id']),
        'comments':Comment.objects.all(),
    }
    return render(request, 'wall_app/comment.html', context)

def stickypost(request):
    Comment.objects.create(message_id=Message.objects.get(id=request.POST['message_id']), comment = request.POST['commentcontent'])
    return redirect('/')
