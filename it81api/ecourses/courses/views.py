from django.shortcuts import render
#
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Lesson, User
from .serializers import CourseSerializer, LessonSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        
        return [permissions.AllowAny()]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    #list(get)
    #...(post)
    #detail
    #...(put)
    #...(delete)
    
    # swagger_schema = None
    
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    
    @swagger_auto_schema(
        operation_description='api nay dung de an 1 bai viet tu phia client',
        responses= {
            status.HTTP_200_OK: LessonSerializer()
        }
    )
    
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

        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)

def index(request):
	return render(request, template_name='index.html', context = {
		'name' : 'inosuke'
	})

