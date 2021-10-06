from django.shortcuts import render
from .models import *
# from .form import *
from django.urls import reverse_lazy
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import *
from .form import *
from django.urls import reverse_lazy
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class PostTemplateView(TemplateView):
    model = Post
    template_name = "index.html"
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        category = Category.objects.all()
        post = Post.objects.all()
        context = {"category":category,"post":post}
        return context


class PostDetailView(TemplateView):
    model = Post
    template_name = 'collection.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data (*args,**kwargs)
        category = Category.objects.all()
        post = Post.objects.all()[3:]
        context = {"category":category,"post":post}
        return context


class PostShoesView(TemplateView):
    model = Post
    template_name = "shoes.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all()
        post = Post.objects.all()
        context = {"category": category, "post": post}
        return context



class PostViews(View):
    def get(self,request):
        categoty = Category.objects.all()
        post = Post.objects.all()
        paginator = Paginator(post,6,orphans=0,allow_empty_first_page=True)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        c = {"post":page.object_list,'page':page,'category':categoty}
        return render(request,'shoes.html',c)


class PostRaceingView(TemplateView):
    models = Post
    template_name = 'racing boots.html'
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        post = Post.objects.all()
        context = {"post":post}
        return context



class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("enjoy:index")
    template_name = 'form.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy("enjoy:index")
    template_name = "form.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("enjoy:index")


class PostDetail(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"