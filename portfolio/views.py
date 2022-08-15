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

def contact(request):
	if request.method == "POST":
		form = ContactForm()
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			print(subject, message, sender)

		#send mail function
		send_mail(
			f'Message Subject: {subject}',#subject
			message,#message
			sender,#fromEmail
			['freakoutbond2@gmail.com'],#ToEmail
			fail_silently=False
			)
		return render(request, 'dashboard.html', {'message': message})
	else:
		return render(request, 'dashboard.html', {})


def resume(request):
    return render(request, 'portfolio/resume.html')

def sendEmail(request):
	if request.method == 'POST':

		template = render_to_string('portfolio/dashboard.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		print(template)
	'''		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['freakoutbond2@gmail.com']
			)
	

		email.fail_silently=False
		email.send()

	'''
	return render(request, 'portfolio/email_sent.html')






