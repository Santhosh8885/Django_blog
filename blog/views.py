from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy,reverse
from .forms import PostForm
from django.views import generic
from django.http import JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin



def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self,**kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)




def about(request):
    return render(request,'blog/about.html',{'title':'About'})


# def PostView(request):

#     form = PostForm()

#     return render(request,'blog/post.html',{'form' : form})

# def addPost(request):
#     if request.is_ajax and request.method == 'POST':
#         form = PostForm(request.POST)

#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             ser_instance = serializers.serialize('json',[instance])

#             return JsonResponse({'instance':ser_instance},status=200)


#         else:

#             return JsonResponse({'error':form.errors},status=400)
#     return JsonResponse({'error':''},status=400)

