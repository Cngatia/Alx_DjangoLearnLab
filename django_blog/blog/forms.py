from django import forms
from .models import Profile,Post,Comment,Tag
from taggit.forms import TagWidget
from django.forms import widgets
from django.contrib.auth.models import User

# can be used to add styling to our forms
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    author = forms.ModelChoiceField(queryset=User.objects.all(),widget=widgets.Select(attrs={'class': 'form-select', 'placeholder': 'author'}))

    
    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control','placeholder': 'Content'}))
    tags = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control'}))

    

    class Meta:
        model = Post
        fields = ['title','author', 'content','tags']
    def form_valid(self, form):
     post = form.save(commit=False)
     post.author = self.request.user
     post.save()
     tags = form.cleaned_data['tags'].split(',')
     for tag_name in tags:
        tag_name = tag_name.strip()
        if tag_name:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
     return super().form_valid(form)   
    def clean_tags(self):
        tag_names = self.cleaned_data['tags']
        return tag_names
    def save(self, commit=True):
        post = super().save(commit=True)
        for tag_name in self.clean_tags():
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return post
class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder': 'Content', 'style': 'font-size: 12px; padding: 16px; height: 80px;'  }))
    class Meta:
        model = Comment
        fields = ['content']