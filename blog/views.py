from django.shortcuts import redirect, render
from .models import Post
from index.models import category,place
from taggit.models import Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def blog_list(request):
    all_posts=Post.objects.all()
    categories=category.objects.all()
    address=place.objects.all()
    tags=Tag.objects.all()
    paginator = Paginator(all_posts, 3)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    last_posts = Post.objects.all().order_by('post_date')[:3]
    return render(request,'blog/blog_list.html',{'posts':all_posts,'categories':categories , 'address':address  ,'tags':tags , 'last_post':last_posts
     })
def post_search(request):
    search_name=request.GET.get('q')
    search_result=Post.objects.filter(
                Q(title__icontains=search_name) |
                Q(content__icontains=search_name)
    )
    categories=category.objects.all()
    address=place.objects.all()
    return render(request,'blog/blog_search.html',{'search_result':search_result , 'categories':categories , 'address':address})
def blog_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'blog/blog_detail.html', {'post':post})
def update_post(request,id):
    single_post=Post.objects.get(id=id)
    if request.method=='POST':
        postfore=PostForm(request.POST,request.FILES,instance=single_post)
        if postfore.is_valid():
            postfore.save()
    else:
        postfore=PostForm(instance=single_post)
    return render(request,'blog/update_post.html',{'postform':postfore})
@login_required
def new_post(request):
    if request.method=='POST':
        postform=PostForm(request.POST,request.FILES)
        if postform.is_valid():
            postform.save()
    else:
        postform=PostForm()
    return render(request,'blog/add_new_post.html',{'postform':postform})
def delete_post(request,id):
    single_post=Post.objects.get(id=id)
    single_post.delete()
    return redirect('index:index')
def like(request,id):
    single_post=Post.objects.get(id=id)
    if request.user in single_post.like.all():
        single_post.like.remove(request.user)
    else:
        single_post.like.add(request.user)
    return redirect('blog:list')
def like_with_ajax(request,id):
    single_post=Post.objects.get(id=id)
    if request.user in single_post.like.all():
        single_post.like.remove(request.user)
        like.value='unlike'
    else:
        single_post.like.add(request.user)
        like.value='like'
    data={
        'value':like.value,
        'likes':single_post.like.all().count()
    }
    return JsonResponse(data,safe=False)