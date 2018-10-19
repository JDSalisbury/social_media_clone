from django.conf.urls import url
from . import views

app_name = 'groups'


urlpatterns = [
    url(regex=r'^/$', views.ListGroups.as_view(), name='all'),
    url(regex=r'^new/$', views.CreateGroup.as_view(), name='create'),
    url(regex=r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]
