from django.db.models import fields
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin,\
    PermissionRequiredMixin
from .models import Course


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.slug == '':
            form.instance.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)


class OwnerCourseMixin(LoginRequiredMixin,
                       PermissionRequiredMixin,
                       OwnerMixin):
    model = Course
    fields = ['subject', 'title', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'