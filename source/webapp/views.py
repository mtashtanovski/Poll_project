from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, ListView

# Create your views here.
from webapp.models import Poll, Choice


class IndexView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'index.html'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        print(context)

        return context

