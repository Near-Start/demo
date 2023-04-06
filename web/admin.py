from django.contrib import admin

# Register your models here.
from .models import Student, Question, Grade


class questionadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'optionA', 'optionB', 'optionC', 'optionD', 'answer', 'score')
    list_filter = ('subject',)
    search_fields = ('title',)
    ordering = ['subject']


class gradeadmin(admin.ModelAdmin):
    list_display = ('sid', 'subject', 'grade', 'time')
    list_filter = ('subject',)
    search_fields = ('title',)
    raw_id_fields = ('sid',)
    date_hierarchy = 'time'
    ordering = ['time', 'sid']


admin.site.register(Student)
admin.site.register(Question, questionadmin)
admin.site.register(Grade, gradeadmin)
