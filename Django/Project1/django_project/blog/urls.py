from django.urls import path
from . import views
from .views import ( PostListView, 
                     PostDetailView, 
                     PostCreateView,
                     PostUpdateView,
                     PostDeleteView,
                     UserPostListView
)

urlpatterns = [
    # path('', views.home, name = 'blog-home'),
    path('', PostListView.as_view(), name = 'blog-home'),

    # for posts of particular user
    path('user/<str:username>/', UserPostListView.as_view(), name = 'user-posts'),

    # for postdetail using django convention
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),

    # to create the post
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),

    # to update the post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),

    # to delete the post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),

    path('about/', views.about, name = 'blog-about')   
]

# generic ListView Looks for a template having pattern <app>/<model>_<viewtype>.html 
# in the case of PostListView it will be /blog/post_list.html