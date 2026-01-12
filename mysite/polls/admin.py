from django.contrib import admin

from .models import Question, Choice

# Keeping choices inline within the Question admin page
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
# customize the admin interface for Question model
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # Add a filter sidebar by publication date
    search_fields = ['question_text'] # fields to search on
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)