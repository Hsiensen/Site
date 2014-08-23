from django.contrib import admin
from Jeapedu_Live.models import *


class IndexAdmin(admin.ModelAdmin):
    list_display =('courses',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)

class CoursesAdmin(admin.ModelAdmin):
    list_display =('cou_theme',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)

class StudentAdmin(admin.ModelAdmin):
    list_display =('stu_name',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)

class TapedAdmin(admin.ModelAdmin):
    list_display =('mov_remarks',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)

class LiveAdmin(admin.ModelAdmin):
    list_display =('upc_content',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)

class ReadyAdmin(admin.ModelAdmin):
    list_display =('ins_linux',)
    class Media:
	js=("http://tinymce.cachefly.net/4.1/tinymce.min.js","/static/js/tiny.js",)



admin.site.register(Index,IndexAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Taped,TapedAdmin)
admin.site.register(Live,LiveAdmin)
admin.site.register(Ready,ReadyAdmin)
