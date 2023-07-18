from .models import Comment, Image
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')