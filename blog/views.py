# blog/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import PostForm


from django.shortcuts import render
from .models import Post

def post_list(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(title__icontains=search_query)
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)



def news(request):
     return render(request, 'blog/news.html')

       
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})