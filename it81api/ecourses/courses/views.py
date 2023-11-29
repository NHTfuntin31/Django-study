from django.shortcuts import render
#
from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    #list(get)
    #...(post)
    #detail
    #...(put)
    #...(delete)
    
    #permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

def index(request):
	return render(request, template_name='index.html', context = {
		'name' : 'inosuke'
	})

