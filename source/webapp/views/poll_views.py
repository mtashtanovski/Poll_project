from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'polls/index.html'
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class PollView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.object.choices.order_by('pk')
        context['choices'] = choices
        print(context)
        return context


class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/poll_create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollEdit(UpdateView):
    form_class = PollForm
    template_name = 'polls/poll_edit.html'
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDelete(DeleteView):
    model = Poll
    template_name = 'polls/poll_delete.html'
    success_url = reverse_lazy('index')
