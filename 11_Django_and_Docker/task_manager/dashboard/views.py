import http
from django import http as dj_http
from django import urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from dashboard import models, forms
from django.contrib.auth import models as auth_models


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['is_manager'] = self.request.user.groups.filter(name='Manager').exists()
        return context_data


class UsersListView(LoginRequiredMixin, generic.ListView):
    model = auth_models.User
    template_name = 'users.html'
    paginate_by = 5

    def get_queryset(self):
        return auth_models.User.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = auth_models.User.objects.count()
        context_data['is_manager'] = self.request.user.groups.filter(name='Manager').exists()
        return context_data

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return super().get(request, args, kwargs)
        else:
            raise dj_http.Http404("Whatever.")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'project_list.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Developer').exists():
            return user.users_project.all()
        return models.Project.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = models.Project.objects.count()
        return context_data


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Project
    template_name = 'project_detail.html'


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_create.html'


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_update.html'


class ProjectDeleteView(generic.DeleteView):
    model = models.Project
    success_url = urls.reverse_lazy('projects-list')
    template_name = 'project_delete.html'


class IssueListView(LoginRequiredMixin, generic.ListView):
    model = models.Issue
    template_name = 'issue_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Issue.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = models.Issue.objects.count()
        return context_data


class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Issue
    template_name = 'issue_detail.html'


class IssueCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Issue
    fields = [
        'name',
        'description',
        'deadline',
        'assigne',
        'project',
        'reported'
    ]
    template_name = 'issue_create.html'


class IssueUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Issue
    fields = [
        'name',
        'description',
        'deadline',
        'assigne',
        'project',
        'reported'
    ]
    template_name = 'issue_update.html'


class IssueDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Issue
    success_url = urls.reverse_lazy('issue-list')
    template_name = 'issue_delete.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.UploadFileForm()
    return render(request, 'upload.html',
                  {
                   'form': form
                  })


class SolarSystemView(generic.TemplateView):
    template_name = 'solar-system.html'

