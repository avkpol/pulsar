from django.shortcuts import render


def steps(request):

	return render(request,'steps.html',locals())


	
