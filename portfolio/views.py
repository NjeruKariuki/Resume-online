from email import message
from re import template
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from users.models import ChiefImage, Skills
from .forms import ContactForm



def portfolio(request):
	projects = Project.objects.all()
	project1 = Project.objects.get(pk=1)
	feature_image = project1.image.url
	#image
	image = ChiefImage.objects.all()[0]
	#skills
	skills = Skills.objects.all()

	context={'projects' : projects,
	 'specialproject' : project1,
	  'feature_image' : feature_image,
	  'image' : image,
	  'skills' : skills
		}

	#var to keep track of form
	messageSent = False
	if request.method == "POST":
		name = request.POST.get('name')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		sender = request.POST.get('sender')
		send_mail(
				f'Message Subject: {subject}',#subject
				message,#message
				settings.EMAIL_HOST_USER,#fromEmail
				['freakoutbond2@gmail.com'],#ToEmail
				fail_silently=False
			)
		messageSent = True
		return HttpResponse(f'Thank you {name} for connecting!')

	return render(request,'portfolio/dashboard.html', context)

def project(request, pk):
	project_images = []
	project = Project.objects.get(pk=pk)	
	technologies = project.technologies.all()
	images = project.images.all()
	f_image = project.image
	for image in images:
		project_images.append(image)

	context = {'project' : project,
	 'technologies' : technologies,
	  'images': project_images,
	  'f_image': f_image
	  }
	return render(request,'portfolio/project.html', context)




def resume(request):	
    return render(request, 'portfolio/resume.html', {})


def contact(request):
	#var to keep track of form
	messageSent = False
	if request.method == "POST":
		name = request.POST.get('name')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		sender = request.POST.get('sender')
		send_mail(
				f'Message Subject: {subject}',#subject
				message,#message
				sender,#fromEmail
				[settings.EMAIL_HOST_USER],#ToEmail
				fail_silently=False
			)
		messageSent = True
		return HttpResponse(f'Thank you {name} for connecting!')

	return render(request, 'portfolio/dashboard.html', {
		 'messageSent': messageSent,
		  })






