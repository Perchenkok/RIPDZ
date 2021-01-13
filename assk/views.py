from django.shortcuts import render,redirect
from assk.models import Account, Post , Answer, Tags
from assk.forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    allQs= Post.objects.all()
    return render(request, 'index.html', {'allqs': allQs})

@login_required
def question(request,pk):
    qs=Post.objects.get(pk = pk)
    answers = Answer.objects.filter(question=qs)
    if request.method == 'GET':
       form = NewAnswer()
    else:
        form = NewAnswer(data=request.POST)
        if form.is_valid():
           
            answer=form.save(commit=False)
            answer.question= Post.objects.get(pk = pk)
            answer.author = Account.objects.get(user=request.user.pk)
            answer.save()
        else:
            form.add_error(None, 'Введите верные данные')
    return render(request, 'inc/question.html' ,{'answers':answers, 'question': qs, 'form':form})

def redirectStartPageIndexPronto(request):
    return redirect('/index/')

@login_required
def newPost(request):
    if request.method == 'GET':
        form = NewPost()
    else:
        form = NewPost(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Account.objects.get(user=request.user.pk)
            tags = form.cleaned_data.get('tags').split()
            #post.tags.set(Tags.objects.filter(name__in=tags))
            post.save()
        else:
            form.add_error(None, 'Введите верные данные')
    ctx = {'form': form}
    return render(request, 'newQuestion.html', ctx)

@login_required
def AddAnswer(request):
    if request.method == 'GET':
        form = NewPost()
    else:
        form = NewPost(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Account.objects.get(user=request.user.pk)
            tags = form.cleaned_data.get('tags').split()
            post.tags.set(Tags.objects.filter(name__in=tags))
            post.save()
        else:
            form.add_error(None, 'Введите верные данные')
    ctx = {'form': form}
    return render(request, 'newQuestion.html', ctx)
