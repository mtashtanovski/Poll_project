from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ChoiceForm
from webapp.models import Poll, Choice


class ChoiceAdd(CreateView):
    model = Choice
    template_name = 'choices/choice_add.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class ChoiceEdit(UpdateView):
    model = Choice
    template_name = 'choices/choice_edit.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class ChoiceDelete(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
