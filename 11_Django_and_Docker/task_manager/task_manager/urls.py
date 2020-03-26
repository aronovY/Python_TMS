"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from dashboard import views
from authentication import views as auth_view
from authentication import api_view
from task_manager import settings


from dashboard import api_views as dash_api_views


router = routers.DefaultRouter()
router.register(r'users', api_view.UserViewSet)
router.register(r'groups', api_view.GroupViewSet)
router.register(r'projects', dash_api_views.ProjectViewSet)
router.register(r'issue/', dash_api_views.IssueViewSet)
urlpatterns = [
    # api

    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        auth_view.LoginView.as_view(),
        name='login'),

    path(
        'login/',
        auth_view.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_view.LogoutView.as_view(),
        name='logout',
    ),

    path(
        'register/',
        auth_view.RegisterFormView.as_view(),
        name='register',
    ),

    # projects
    path(
        'home/',
        views.IndexView.as_view(),
        name='index'
    ),

    path(
        'users/',
        views.UsersListView.as_view(),
        name='users'
    ),

    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects-list'
    ),
    path(
        'projects/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='projects-detail'
    ),
    path(
        'projects/create/',
        views.ProjectCreateView.as_view(),
        name='projects-create'
    ),
    path(
        'projects/<int:pk>/update/',
        views.ProjectUpdateView.as_view(),
        name='projects-update'
    ),
    path(
        'projects/<int:pk>/delete/',
        views.ProjectDeleteView.as_view(),
        name='projects-delete'
    ),

    path(
        'issue/',
        views.IssueListView.as_view(),
        name='issue-list'
    ),

    path(
        'issue/<int:pk>/',
        views.IssueDetailView.as_view(),
        name='issue-detail'
    ),

    path(
        'issue/create/',
        views.IssueCreateView.as_view(),
        name='issue-create'
    ),

    path(
        'issue/<int:pk>/update/',
        views.IssueUpdateView.as_view(),
        name='issue-update'
    ),

    path(
        'issue/<int:pk>/delete/',
        views.IssueDeleteView.as_view(),
        name='issue-delete'
    ),
    path(
        'upload/',
        views.model_form_upload,
        name='upload'
    ),

    path(
        'solar-system',
        views.SolarSystemView.as_view(),
        name='solar-system',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
