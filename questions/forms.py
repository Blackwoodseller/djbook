from django import forms

from questions.models import Question, QuestionComment



class NewQuestionForm(forms.ModelForm):
    question_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Question title',
                                                                   'class': 'form-control', 'required':True,
                                                                   'autofocus':True}))

    question_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Question text',
                                                                 'class': 'form-control', 'required':True,
                                                                 'rows': '10', 'style':'height: 138px'}))

    class Meta(object):
        model = Question
        fields = ['question_title', 'question_text', ]


class NewCommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Put your comment here',
                                                                 'class': 'form-control', 'required':True,
                                                                 'rows': '10', 'style':'height: 138px'}))

    class Meta(object):
        model = QuestionComment
        fields = ['comment_text', ]
