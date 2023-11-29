from django.urls import path, include
from . import views
# from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', views.CourseViewSet)

# /courses/ -get
# /courses/ -post
# /courses/{course_id}/ -get
# /courses/{course_id}/ -put
# /courses/{course_id}/ -delete

urlpatterns = [
    path('', include(router.urls)),
]
