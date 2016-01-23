from django.shortcuts import  HttpResponse
from django.contrib.auth.decorators import login_required

import subprocess
from subprocess import Popen, PIPE

import json
import fileinput
import os
import os.path

dangerMsg = "Server error! Please try again later"
warnMsg = "User is not autentificated!Please either signup or login!"
warnMsg2 = "There is no proper line! Check file content."
successMsg = "Key was succesfully generated an tested!"
successMsg2 = "Keys and certificates were successfully generated"
successMsg3 = 'User server data were edited'

def runKeyGenProcess(request):
	''' runs  secret key generation and testing process'''
	
	req_user = request.user
	openKeyGen = ('cd /etc/openvpn && openvpn --genkey --secret key_' + str(req_user))
	openKeyTest = ('cd /etc/openvpn && openvpn --test-crypto --secret key_' + str(req_user))
	if request.user.is_authenticated():
		if request.method == 'POST': 
			givePerm = subprocess.Popen("chmod -R ugo+rw /etc/openvpn",shell=True)
			subprocess.Popen(openKeyGen, shell=True)
			subprocess.Popen(openKeyTest, shell=True)
		return HttpResponse(successMsg)
	
	return HttpResponse(warnMsg)

def runStep3Process(request):
	'''collect data from step3 user form and insert 
	them in '/etc/openvpn/easy-rsa/vars'
	'''
	path = '/etc/openvpn/easy-rsa/vars'
	
	data = json.loads(request.body)
	
	key_country = 'export KEY_COUNTRY="%s"' % data['key_country']
	key_province = 'export KEY_PROVINCE="%s"' % data['key_province']
	key_city = 'export KEY_CITY="%s"' % data['key_city']
	key_org = 'export KEY_ORG="%s"' % data['key_org']
	key_cn = 'export KEY_CN="%s"' % data['key_cn']
	key_email = 'export KEY_EMAIL=%s' % data['key_email']
		
	if request.method=='POST' and request.user.is_authenticated():
		
		with open(path) as varsfile:
		    data = varsfile.readlines()
		try:
			data[63] = key_country +'\n' 
			data[64] = key_province +'\n' 
			data[65] = key_city +'\n' 
			data[66] = key_org +'\n'
			data[67] = key_email +'\n' 
			data[69] = key_cn +'\n' 
			
			with open(path, 'w') as newvarsfile:
				newvarsfile.writelines(data)
				pass3Cmds()
				# check if files exist in '/etc/openvpn/easy-rsa/keys
				servCrt = '/etc/openvpn/easy-rsa/keys/%s.crt' % key_cn
				servCsr= '/etc/openvpn/easy-rsa/keys/%s.csr' % key_cn
				servKey = '/etc/openvpn/easy-rsa/keys/%s.key' % key_cn
				# pem = '/etc/openvpn/easy-rsa/keys/dh1024.pem '
				keys = (servCrt, servCsr, servKey)
				
				for key in keys:
					if os.path.isfile(key):

						return HttpResponse(successMsg)
					return HttpResponse(successMsg2)
									
		except IndexError:
			return HttpResponse(warnMsg2)
	
	return HttpResponse(warnMsg)

def pass3Cmds():
	''' run commands on step3  to generate keys and cert in '/etc/openvpn/easy-rsa/keys'
	'''
	permission = "cd /etc/openvpn/easy-rsa && chmod -R ugo+rwx /etc/openvpn/easy-rsa"
	cmds = "cd /etc/openvpn/easy-rsa && . ./vars && ./clean-all && ./pkitool --initca && ./pkitool --server && ./build-dh"
	givePm = subprocess.Popen(permission, shell=True)
	runCmds = subprocess.Popen(cmds, shell=True)

			
	return (givePm, runCmds) 
	
def runStep4Process(request):
	'''collects data from step4 user form and inserts 
	them in '/etc/openvpn/server.conf'
	'''
	path = '/etc/openvpn/server.conf'
	data = json.loads(request.body)

	serv_port = '%s' % data['port']
	serv_mask = '%s' % data['servmsk']
	serv_ip = '%s' % data['servip']

	if request.method=='POST' and request.user.is_authenticated():
		
		with open(path) as conf:
		    data = conf.readlines()
		try:
			data[31] = '#' +'\n'
			data[32] = serv_port +'\n'
			data[116] = serv_ip + serv_mask +'\n' 
			with open(path, 'w') as newconf:
				newconf.writelines(data)
				return HttpResponse(successMsg3)				
		except IndexError:
			return HttpResponse(warnMsg2)

	return HttpResponse(warnMsg)

