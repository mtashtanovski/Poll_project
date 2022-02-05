from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
from webapp.models import Poll, Choice
from webapp.forms import PollForm


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


class PollView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        context['poll'] = poll
        return context


class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll_create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollEdit(UpdateView):
    form_class = PollForm
    template_name = 'poll_edit.html'
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDelete(DeleteView):
    model = Poll
    template_name = 'poll_delete.html'
    success_url = reverse_lazy('index')
