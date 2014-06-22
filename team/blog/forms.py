from django import forms
from models import Post, Comment
from django.utils import timezone

class BlogForm(forms.Form):
    id = forms.CharField(required = False, widget = forms.HiddenInput())
    title = forms.CharField(max_length = 140)
    description = forms.CharField(max_length=140)
    content = forms.CharField(widget=forms.widgets.Textarea() ) 
    slug  = forms.BooleanField(required=False)
    author = forms.CharField(required = True)
    link = forms.URLField(required=True)
    link_description = forms.CharField(max_length = 140 , required = True)

    def save(self):
        data = self.cleaned_data
        published_date = timezone.now()
        if data['id']:  # update
            p = Post.objects.filter(id = data['id'])
            if p:
                p = p[0]
                p.title = data['title']
                p.description = data['description']
                p.content = data['content']
                p.slug = data['slug'] and True or False
                p.published = published_date
                p.author = data['author']
                p.link = data['link']
                p.link_description = data['link_description']
                p.save()
        else:   # add
            p = Post(title = data['title'], description = data['description'], content = data['content'], slug = data['slug'] and True or False, published = published_date, author = data['author'], link = data['link'], link_description = data['link_description'])
            p.save()
        return True

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20)
    text = forms.CharField(max_length = 200)

    def save(self):
        data = self.cleaned_data
        timestamp = timezone.now()
        c = Comment( name = data['name'], text = data['text'] )
        c.save()


