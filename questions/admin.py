from django.contrib import admin
from questions.models import Question, QuestionComment

class CommentInline(admin.TabularInline):
    model = QuestionComment
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author', {'fields': ['author']}),
        ('Question title', {'fields': ['question_title']}),
        ('Question text', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # inlines = [CommentInline]
    list_display = ['author', 'question_title', 'question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)