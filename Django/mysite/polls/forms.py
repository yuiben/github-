from importlib.resources import contents
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','time_create',)
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'tieude'}),
            'content' : forms.Textarea(attrs={'class': 'Noi_dung_ne'})
        }
        

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'con-tent', 'id' : 'noidung'}))
    cc = forms.BooleanField()
    