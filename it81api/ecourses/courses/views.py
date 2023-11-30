from django.shortcuts import render
#
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
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


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    
    #an lesson (active=flase)
    @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    #lessons/{pk}/hide-lesson
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Response(data=LessonSerializer(l).data, status=status.HTTP_200_OK)

def index(request):
	return render(request, template_name='index.html', context = {
		'name' : 'inosuke'
	})

