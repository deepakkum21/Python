from django.shortcuts import render
from django.views.generic import (ListView, 
                        DetailView,
                        CreateView,
                        UpdateView,
                        DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.
# function based views
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based view
class PostListView(ListView):
    model = Post

    # by deafault the generic ListView template will be app/post_list.html follow pattern of <app>/<model>_<viewtype>.html
    # since we are not having by default app/post_list.html template and if we want to manually change the name of the template
    # then have to extensively define it as template_name and pass the value of the template which you want to render
    template_name = 'blog/home.html'

    # created the var on which to loop as by deafult it stores as ObjectList
    context_object_name = 'posts'

    # to order the posts by latest prefix - 
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    
    model = Post
    # by deafault the generic DetailView template will be app/post_detail.html follow pattern of <app>/<model>_<viewtype>.html
    # since we are following the django convention so no need to manually set the template name to blog/post_detail.html
    # it will automatically route to the template blog/post_detail.html

    # while accesing the post in the template it will be aclled as object and if want to change it then have to pass value for 
    # context_object_name = 'post'



# LoginRequiredMixin is required so that without loging no-one can create a new post
# in function based view this can be done using @login_required
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # by deafault the generic CreateView template will be not be by convention type beacuse the create and update generic view 
    # will use same template i.e. <app>/<model>_<form>

    # overriding form_valid() 
    # to prevent the integrity error as form is naot able to get author name which should be the current logged user
    def form_valid(self, form):

        # setting the author from the request to the form instance
        form.instance.author = self.request.user

        # need to call the super form_valid() to validate the form
        return super().form_valid(form)


# LoginRequiredMixin is required so that without loging no-one can create a new post
# in function based view this can be done using @login_required
# UserPassesTestMixin is used to see wheather the same logged in user is updating his records only not others
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # by deafault the generic CreateView template will be not be by convention type beacuse the create and update generic view 
    # will use same template i.e. <app>/<model>_<form>

    # overriding form_valid() 
    # to prevent the integrity error as form is naot able to get author name which should be the current logged user
    def form_valid(self, form):

        # setting the author from the request to the form instance
        form.instance.author = self.request.user

        # need to call the super form_valid() to validate the form
        return super().form_valid(form)

    # this func will have the logic to see that the logged in user is updating his own stuff not others
    def test_func(self):
        # to get the current post
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

# LoginRequiredMixin is required so that without loging no-one can create a new post
# in function based view this can be done using @login_required
# UserPassesTestMixin is used to see wheather the same logged in user is updating his records only not others
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post

    # redirecting to home page when the post is successfully deleted
    success_url = '/'

    # by deafault the generic DeleteView template will have the template <app>/<model>_confirm_delete.html i.e. blog/post_confirm_delete.html

    # this func will have the logic to see that the logged in user is updating his own stuff not others
    def test_func(self):
        # to get the current post
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
