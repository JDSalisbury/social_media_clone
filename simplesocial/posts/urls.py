from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(regex=r'^$', views.PostList.as_view(), name='all'),
    url(regex=r'^new/$', views.CreatePost, name='create'),
    url(regex=r'^by/(?P<username>)$', views.UserPosts.as_view(), name='for_user'),
    url(regex=r'^by/(?P<username>)$/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='single'),
    url(regex=r'^delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete'),
]
