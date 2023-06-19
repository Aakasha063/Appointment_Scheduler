from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm
from .models import BlogPost, Category
from django.contrib.auth.decorators import login_required, permission_required


def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/veiw_blog.html', {'blog_post': blog_post})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            if 'save_draft' in request.POST:
                blog_post.draft = True
            blog_post.save()
            return redirect('blog:doctor_view_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def patient_view_blog_posts(request):
    blog_posts = BlogPost.objects.filter(draft=False)
    categories = Category.objects.all()
    context = {'categories': categories, 'blog_posts': blog_posts}
    return render(request, 'blog/patient_view_blog_posts.html', context)

@login_required
def doctor_view_blog_posts(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_view_blog_posts.html', {'blog_posts': blog_posts})
