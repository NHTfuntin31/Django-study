from django.contrib import admin
#them
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
# Register your models here.

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
        
class LessonTagInline(admin.StackedInline):
# class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through

class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
			'all': ['/static/css/main.css', ]
		}
        #js
    form = LessonForm
    list_display = ["id", "subject", "created_date", "active" ,"course"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInline, )
    
    def avatar(self, lesson):
        return mark_safe('''
			<img src='/static/{img_url}' alt='{alt}' width='50px'/>
        '''.format(img_url=lesson.image.name, alt=lesson.subject))
        
        
class LessonInline(admin.StackedInline):
	model = Lesson
	pk_name = 'course'
        
        
class CourseAdmin(admin.ModelAdmin):
	inlines = (LessonInline, )


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY KHOA HOC'
    
    def get_urls(self):
        return [
			path('course-stats/', self.course_stats)
		] + super().get_urls()
    
    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values("id", "subject", "lesson_count")
        
        return TemplateResponse(request, 'admin/course-stats.html', {
			'course_count': course_count,
			'stats': stats,
		})
    
admin_site = CourseAppAdminSite('mycourse')

# admin_site.register(Category)
# admin_site.register(Course, CourseAdmin)
# admin_site.register(Lesson, LessonAdmin)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(User)
admin.site.register(Permission)
