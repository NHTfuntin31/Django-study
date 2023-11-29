from django.shortcuts import render
#
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
	return render(request, template_name='index.html', context = {
		'name' : 'inosuke'
	})


def welcome(request, year):
    return HttpResponse("hello" + str(year))

def welcome2(request, year):
    return HttpResponse("hello2" + str(year))

class TestView(View):
    def get(self, request):
        return HttpResponse("Testing")
    
    def post(self, request):
        pass