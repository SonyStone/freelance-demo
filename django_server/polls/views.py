from django.http import HttpResponse

def index(rqeuest):
	return HttpResponse("Hello, world. You're at the polls index.")
