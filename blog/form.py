from django import forms
from .models import *
from django.forms import modelform_factory

PostForm = modelform_factory(Post,fields=("category","name","old_price","price","image","desc",))


class CreatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='category',
                                      widget=forms.widgets.Select(attrs={"size":1,"class":"form-control"}))
    class Meta:
        model = Post
        fields = ("category","name","old_price","price","image","desc")