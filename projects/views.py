from django.shortcuts import render
from django.views import generic
from .models import Project, Photo
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'projects'
    template_name = 'index.html'
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data["photos"] = Photo.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        return data
    