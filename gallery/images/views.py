# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageForm

# Create your views here.


def image_upload(request):
    form = ImageForm(request.POST or None, request.FILES or None)

    if not request.FILES:
        messages.error(request, "Выберите файл")

    try:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
    except KeyError:
        messages.error(request, "Не подходящий тип файла!")

    context = {
        "form": form
    }

    return render(request, "image_upload.html", context)


def image_list(request):
    queryset = Image.objects.all()
    context = {
        "object_list": queryset,
        "title": "Галерея",
    }
    return render(request, "image_list.html", context)