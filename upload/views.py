
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django import forms
from .forms import *
from .models import images
from django.db import IntegrityError

# Create your views here.
def image_view(request):

	if request.method == 'POST':
		form = image_Form(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('image_upload')
	else:
		form = image_Form()
	return render(request, 'upload/upload.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')


def detail(request, images_pk):

    #img = get_object_or_404(images, pk=images_pk)
    if request.method == 'GET':
        img = images.objects.filter(pk=images_pk)
        return render(request,'upload/detail.html',{"img":img})

# Create your views here.
# Python program to view
# for displaying images

def display_images(request):

    if request.method == 'GET':
		 # getting all the objects of hotel.
        display_images = images.objects.all()
        return render(request, 'upload/display_images.html', {'display_images' : display_images})
