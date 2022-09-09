from logging import PlaceHolder
from mimetypes import init
from django import forms
from freddit.models import Thread, Comment

class ThreadForm(forms.ModelForm):
    topic = forms.CharField(widget=forms.Textarea(attrs={'class': 'topic_form', 'rows': 2, 'cols': 100}), max_length=200, help_text="Post Topic:")
    inform = forms.CharField(widget=forms.Textarea(attrs={'rows': 30, 'cols': 120}))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.CharField(widget=forms.HiddenInput(), initial="anonymous")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Thread
        fields = ('topic', 'inform', )

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.CharField(widget=forms.HiddenInput(), initial='anonymous')

    class Meta:
        model = Comment
        exclude = ('thread', )