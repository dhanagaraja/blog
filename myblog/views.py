from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Category
from django.views.generic import ListView, DeleteView, DetailView,CreateView, UpdateView
from .forms import EditForm
from members.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#def main(request):
#    return render(request, 'index.html',{})

class HomeView(ListView):
    model=Post
    template_name= 'index.html'
    ordering = ['-id']
    
    
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       profile = Profile.objects.all()
       context = super(HomeView, self).get_context_data(*args, **kwargs)
       context['cat_menu']=cat_menu
       context['profile']=profile
       return context
    
''' 
class ArticleDetailView(DetailView):
    model=Post
    template_name= 'article_detail.html'
    ordering = ['-stamp']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        profile = Profile.objects.all()
        Posts = Post.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['profile']=profile
        context['Posts'] = Posts
        return context
 '''
def ArticleDetailView(request, cats, pk):
    cat_menu = Category.objects.all()
    profile = Profile.objects.all()
    Posts = Post.objects.all().filter(pk=pk)
    category = Post.objects.all().filter(category__category=cats)
        
    return render(request, 'article_detail.html', {"cat_menu":cat_menu,"profile":profile,"Posts":Posts,"category":category})


class AddPostView(CreateView):
    model=Post
    form_class = EditForm
    template_name = 'add-post.html'
    #fields= '__all__'
    def get_context_data(self,  *args, **kwargs):
        cat_menu = Category.objects.all()
        profile = Profile.objects.all()
        Posts = Post.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['profile']=profile
        context['Posts'] = Posts
        return context


class UpdatePostView(UpdateView):
    model=Post
    form_class = EditForm
    template_name = 'update-post.html'
    #fields= ['title','body',]
    def get_context_data(self,  *args, **kwargs):
        cat_menu = Category.objects.all()
        profile = Profile.objects.all()
        Posts = Post.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['profile']=profile
        context['Posts'] = Posts
        return context


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self,  *args, **kwargs):
        cat_menu = Category.objects.all()
        profile = Profile.objects.all()
        Posts = Post.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['profile']=profile
        context['Posts'] = Posts
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'
    
    def get_context_data(self,  *args, **kwargs):
        cat_menu = Category.objects.all()
        profile = Profile.objects.all()
        Posts = Post.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['profile']=profile
        context['Posts'] = Posts
        return context

def CategoryView(request,cats):
    catagory = Post.objects.filter(category__category=cats)
    category_head = Post.objects.filter(category__category=cats).order_by("stamp")
    cat_menu = Category.objects.all()
    profile = Profile.objects.all()
    context = {'cats':cats, 'category':catagory, "cat_menu":cat_menu, "profile":profile,"category_head":category_head }
    return render(request, 'categories.html', context)

def EditView(request, cats):
    catagory = Post.objects.filter(category__category=cats)
    cat_menu = Category.objects.all()
    profile = Profile.objects.all()
    context = {'category':catagory, "cat_menu":cat_menu, "profile":profile }
    return render(request, 'edit-view.html', context)





