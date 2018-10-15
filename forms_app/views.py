from django.shortcuts import render, redirect
from .models import FormModel
from datetime import datetime


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)


def post_new(request):
    if request.method == "POST":
        form = FormModel(request.POST)
        if form.is_valid():
            post = form.save()
            post.name = request.user
            post.recipe = request.user
            post.timeCook = request.user
            post.dateCreated = datetime
            post.save()
            return redirect('index', pk=post.pk)
    else:
        form = FormModel()
    return render(request, 'forms_app/index.html')
