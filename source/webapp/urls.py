from django.urls import path


from webapp.views import (IndexView,
                          PollView,
                          PollCreate,
                          PollEdit,
                          PollDelete
                          )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(template_name='poll_view.html'), name='poll_view'),
    path('poll/create/', PollCreate.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/', PollEdit.as_view(), name='poll_edit'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete')
]