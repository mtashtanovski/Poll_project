from django.urls import path

from webapp.views.choice_views import ChoiceAdd, ChoiceEdit, ChoiceDelete
from webapp.views.poll_views import (IndexView,
                                     PollView,
                                     PollCreate,
                                     PollEdit,
                                     PollDelete
                                     )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(template_name='polls/poll_view.html'), name='poll_view'),
    path('poll/create/', PollCreate.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/', PollEdit.as_view(), name='poll_edit'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
    path('poll/<int:pk>/choices/add/', ChoiceAdd.as_view(), name="choice_add"),
    path('choice/<int:pk>/edit/', ChoiceEdit.as_view(), name="choice_edit"),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name="choice_delete"),
]