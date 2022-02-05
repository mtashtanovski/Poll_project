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


# class CommentUpdateView(UpdateView):
#     model = Comment
#     template_name = 'comments/update.html'
#     form_class = CommentForm
#
#     def get_success_url(self):
#         return reverse("article_view", kwargs={"pk": self.object.article.pk})
#
#
# class CommentDeleteView(DeleteView):
#     model = Comment
#
#     def get(self, request, *args, **kwargs):
#         return super().delete(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse("article_view", kwargs={"pk": self.object.article.pk})
