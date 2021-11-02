from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/users/$', views.UserList.as_view()),  # list of users
    url(r'^api/users/create/$', views.UserCreate.as_view()),  # create user
    url(r'^api/auth/login/$', views.loginUser.as_view()),  # login user
    url(r'^api/auth/logout/$', views.logoutUser.as_view()),  # logout user
    url(r'^api/services/$', views.ServiceList.as_view()),  # list of services
    url(r'^api/services/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view()),
]
