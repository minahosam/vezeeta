from django import forms
from .models import Post,comments,reply
class PostForm(forms.ModelForm):
    class Meta:                              
        model=Post
        fields='__all__'
class commentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields= ['content']    
class replyform(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':2}),label='')
    content=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'add reply....'}))
    class Meta:
        model=reply
        fields=['content',]