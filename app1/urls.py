from django.urls import path
from .views import Post_view, Post_detail, Create_Post, Edit_view, user_logout

urlpatterns=[
    path('post/<int:pk>/edit',Edit_view.as_view(),name = 'editpost'),
    path('post/new', Create_Post.as_view(), name='newpost'),
    path('/post/<int:pk>',Post_detail.as_view(), name ='detailpost' ),
    path('',Post_view.as_view(),name='homepage'),
    path('logout',user_logout, name='logout'),

]