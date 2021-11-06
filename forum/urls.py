from django.conf.urls import url
from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    url(r'^login/$', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    url(r'^logout', auth_views.LogoutView.as_view(template_name='forum/login.html'), name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^forum/$', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('social-auth/', include('social_django.urls', namespace="social")),
)
