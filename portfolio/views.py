from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project


def portfolio(request):
	projects = Project.objects.all()
	project1 = Project.objects.get(pk=1)
	project_images = list(project1.images.all())
	feature_image = project_images[0].name

	#dictionary to store project name and first image
	proj_dicts, proj_images, proj_names = [], [], []

	for project in projects:
		project.name = {'name': project.name, 'image' : list(project.images.all())[0]}
		proj_dicts.append(project.name)

	for p in proj_dicts:
		proj_images.append(p['image'])

	print(proj_images)
	for img in proj_images:
		ob = list(img.project_set.all())
		for i in ob:
			proj_names.append(i)
			break

	print(proj_names)
	'''
	for project in projects:
		for img in proj_images:
				if project.name == 
					print(img)
		break
'''
	context={'projects' : projects,
	 'specialproject' : project1,
	  'feature_image' : feature_image,
	   'proj_dicts' : proj_dicts,
	    'proj_images' : proj_images,
		'proj_names' : proj_names
		}

	return render(request,'portfolio/dashboard.html', context)

def project(request, pk):
	project_images = []
	project = Project.objects.get(pk=pk)	
	technologies = project.technologies.all()
	images = project.images.all()
	for image in images:
		project_images.append(image)

	context = {'project' : project, 'technologies' : technologies, 'images': project_images}
	return render(request,'portfolio/project.html', context)

def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message = request.POST['message']

		#send mail function
		send_mail(
			'message from ' + message_name,#subject
			message,#message
			message_email,#fromEmail
			['freakoutbond2@gmail.com'],#ToEmail
			fail_silently=False
			)
		return render(request, 'portfolio-home', {'message_name': message_name})
	else:
		return render(request, 'portfolio/contact.html', {})


def resume(request):
    return render(request, 'portfolio/resume.html')

def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('portfolio/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['freakoutbond2@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'portfolio/email_sent.html')