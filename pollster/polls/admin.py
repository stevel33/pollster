from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# This is where I can add admin functionality
# admin.site.register(Question)
# admin.site.register(Choice)

# Tabular Inline to associate choices with questions in adminscreen

admin.site.site_header = "pollster admin"
admin.site.site_title = "pollster admin area"
admin.site.index_title = "welcome to pollster"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), 
    ('the date', {'fields': ['pub_date'], 'classes': ['collapse']})]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# we no longer will have choices on admin Polls section