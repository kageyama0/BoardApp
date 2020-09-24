from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms import CommentCreateForm
from .models import PostModel, CommentModel

class IndexView(ListView):
    template_name = 'pages/index.html'
    model = PostModel
    queryset = PostModel.objects.order_by('-pub_date')
    paginate_by = 10
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    template_name = 'pages/article-detail.html'
    model = PostModel
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = CommentModel.objects.filter(target_id=self.kwargs['pk'])
        return context


class PostView(CreateView):
    template_name = 'pages/post.html'
    model = PostModel
    fields = ('title', 'body')
    success_url = reverse_lazy('index')


class CommentCreateView(CreateView):
    template_name = 'pages/comment-post.html'
    model = CommentModel
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(PostModel, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('post_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        return context
