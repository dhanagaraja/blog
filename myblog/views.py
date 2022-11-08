from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Category
from django.views.generic import ListView, DeleteView, DetailView,CreateView, UpdateView
from .forms import EditForm

# Create your views here.
#def main(request):
#    return render(request, 'index.html',{})

class HomeView(ListView):
    model=Post
    template_name= 'index.html'
    ordering = ['-id']
    menu = Category.objects.all()
    
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(HomeView, self).get_context_data(*args, **kwargs)
       context['cat_menu']=cat_menu
       return context
    

class ArticleDetailView(DetailView):
    model=Post
    template_name= 'article_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context

class AddPostView(CreateView):
    model=Post
    template_name = 'add-post.html'
    fields= '__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class = EditForm
    template_name = 'update-post.html'
    #fields= ['title','body',]
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'

def CategoryView(request,cats):
    catagory = Post.objects.filter(category__category=cats)
    cat_menu = Category.objects.all()
    return render(request, 'categories.html', {'cats':cats, 'category':catagory, "cat_menu":cat_menu })



