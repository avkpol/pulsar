from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, RequestContext
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required

from django.http import HttpRequest

# from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages

import subprocess
from subprocess import Popen, PIPE
# import os


# @login_required	
# @csrf_exempt	
def runKeyGenProcess(request):
	# request.user.is_autentificated():
	req_user = request.user


	openKeyGen = 'cd /etc/openvpn/ && openvpn --genkey --secret key_%s' %(req_user)
	openKeyTest = 'cd /etc/openvpn/ && openvpn --test-crypto --secret key_%s' %(req_user)
	if request.method == 'POST':
		subprocess.Popen(openKeyGen, shell=True)
		subprocess.Popen(openKeyTest, shell=True)
		
		return HttpResponse("Ok : ")

# def runTestSSL_TLS (request):
# 	# request.user.is_autentificated():
	


# 	keyGen = 'cd /etc/openvpn/ && openvpn --genkey --secret key_%s' %(req_user)
# 	keyTest = 'cd /etc/openvpn/ && openvpn --test-crypto --secret key_%s' %(req_user)
# 	if request.method == 'POST':
# 		subprocess.Popen(keyGen, shell=True)
# 		subprocess.Popen(keyTest, shell=True)
		
# 		return HttpResponse("Ok : ")






# @csrf_exempt	
# def runKeyGenProcess(request):
# 	if request.user.is_autentificated()
# 		req_user = request.user
		
		# cmd = 'openvpn --genkey --secret %s' %(req_user,)
# 	else:
# 		return HttpResponseForbidden()

# 	# print request
# 	if request.method == 'POST':
# 		subprocess.Popen('cd /var/www/pulsarvoip && mkdir keys555', shell=True)
# 		subprocess.Popen(cmd, shell=True)
# 		return HttpResponse("Ok")
	
    
# pid = subprocess.Popen(keyGen, shell=True).pid
# 		pid = subprocess.Popen(keyGen, shell=True).pid
# 		return HttpResponse("Ok : "+ str(pid))
	



	# return render(request, '/step1.html/', RequestContext(request, locals()))
	# return render(request,'step1.html',locals())



# def runscript_step1():
# 	print "run script"
	
# 	# script= subprocess.Popen(['sh /var/www/pulsarvoip/src/static/scripts/server_beep.sh',],stdout=PIPE) 

# 	subprocess.Popen('cd /var/www/pulsarvoip && mkdir keys33', shell=True)
# 	# os.system("cd /var/www/pulsarvoip && mkdir keys")
# 	# os.popen("cd /var/www/pulsarvoip && mkdir keys")
# 	# print script
# 	# # output = Popen(['ls', '-l'], stdout=PIPE).communicate()[0]
# 	# message = messages.success(request, "You just loaded your profile initial data")

# @csrf_exempt
# def step1_scr(request):

# 	if request.method == 'POST':
# 		runscript_step1()
	
	
# 	return HttpResponse('Ok')
# 	# return HttpResponseRedirect('step1.html',{'message':message})


