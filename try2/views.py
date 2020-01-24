from __future__ import unicode_literals
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Fields


# Create your views here.
class calculateResult(APIView):

	permission_classes = (IsAuthenticated,)

	def get(self,request):	
		
		operand1 = request.data.get('operand1',"")
		operand2 = request.data.get('operand2',"")
		
		#operand1 = float(operand1)
		#operand2 = float(operand2)
		
		if(operand1 == "" or operand2 == ""):
			return HttpResponse("Operands not specified")
			
		#try:
		#	res = Fields.objects.get(operand1 = 'operand1', operand2 = 'operand2', operator = '+')
		#	myres = Fields.objects.values_list('total', flat = True)
		#	return HttpResponse(myres)
			
		#except Fields.DoesNotExist:
		result = operand1 + operand2
	#		result = int(result)
	#	result1 = Fields.objects.create(operand1 = 'operand1', operand2 = 'operand2', operator = '+', total = 'result')
	#	result1.save()
			
		return HttpResponse(result)
		
	def put(self,request):
	
		operand1 = int(float(request.data.get('operand1',"")))
		operand2 = int(float(request.data.get('operand2',"")))
		
		#operand1 = float(operand1)
		#operand2 = float(operand2)
		
		if(operand1 == "" or operand2 == ""):
			return HttpResponse("Operands not specified")
			
		#try:
		#	res = Fields.objects.get(operand1 = 'operand1', operand2 = 'operand2', operator = '+')
		#	myres = Fields.objects.values_list('total', flat = True)
		#	return HttpResponse(myres)
			
		#except Fields.DoesNotExist:
		result = int(operand1 - operand2)
		#	#result = int(result)
		#	result1 = Fields.objects.create(operand1 = 'operand1', operand2 = 'operand2', operator = '-', total = 'result')
		#	result1.save()
			
		return HttpResponse(result)
		
	def post(self,request):
	
		operand1 = int(float(request.data.get('operand1',"")))
		operand2 = int(float(request.data.get('operand2',"")))
		
		#operand1 = float(operand1)
		#operand2 = float(operand2)
		
		if(operand1 == "" or operand2 == ""):
			return HttpResponse("Operands not specified")
			
		#try:
		#	res = Fields.objects.get(operand1 = 'operand1', operand2 = 'operand2', operator = '+')
		#	myres = Fields.objects.values_list('total', flat = True)
		#	return HttpResponse(myres)
			
		#except Fields.DoesNotExist:
		result = int(operand1 * operand2)
			#result = int(result)
		#	result1 = Fields.objects.create(operand1 = 'operand1', operand2 = 'operand2', operator = '*', total = 'result')
		#	result1.save()
			
		return HttpResponse(result)
		
	def delete(self,request):
		
	
		operand1 = int(float(request.data.get('operand1',"")))
		operand2 = int(float(request.data.get('operand2',"")))
		
		#operand1 = float(operand1)
		#operand2 = float(operand2)
		
		if(operand1 == "" or operand2 == ""):
			return HttpResponse("Operands not specified")
			
		#try:
		#	res = Fields.objects.get(operand1 = 'operand1', operand2 = 'operand2', operator = '+')
		#	myres = Fields.objects.values_list('total', flat = True)
		#	return HttpResponse(myres)
			
		#except Fields.DoesNotExist:
		if(operand2 == 0):
			return HttpResponse("Division by 0 not possible")
		result = int(operand1/operand2)
		#	result1 = Fields.objects.create(operand1 = 'operand1', operand2 = 'operand2', operator = '/', total = 'result')
		#	result1.save()
			
		return HttpResponse(result)
		
