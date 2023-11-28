from django.contrib import admin
#them
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

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
    
    def avatar(self, lesson):
        return mark_safe('''
			<img src='/static/{img_url}' alt='{alt}' width='50px'/>
        '''.format(img_url=lesson.image.name, alt=lesson.subject))


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
