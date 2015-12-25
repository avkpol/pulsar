from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, RequestContext
from django.shortcuts import render
from django.views.generic import View
from pulsarvpn.models import SecretKeys


import os
import subprocess
from subprocess import Popen, PIPE
# import pexpect
# import sh
# from sh import tail

def welcome(request):

	return render(request,'welcomepage.html',locals())


def step1(request):

	return render(request,'step1.html',locals())


def step3(request):

	return render(request,'step3.html',locals())


	





def generate_keys(request):
	# path = "STATICFILES_DIRS.scripts.openvpn.sh"
	path = "/volumes/storage/_codework/erikdd/src/static/scripts/openvpn.sh"
	proc = Popen(
    	"bash /volumes/storage/_codework/erikdd/src/static/scripts/openvpn.sh",
    	shell=True, stdout=PIPE, stderr=PIPE
    )
	proc1 = Popen("openvpn --genkey --secret key", shell=True, stdout=PIPE, stderr=PIPE )
	proc1.wait()    # wait for end process
	res = proc.communicate()  # get tuple('stdout res', 'stderr res')
	# result = proc.stdout.readlines()
	# text = proc.stdout.read()
	res1 = proc1.communicate()
	print proc1, res1
	# send_mail('Subject here', 'Here is the message.', 'mail1@gmail.com', ['mail2@gmail.com'], fail_silently=False)
	return HttpResponse()