from django import forms
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []
        widgets = {
            'question': forms.TextInput(attrs={'class': 'myfieldclass'})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = (
            'option',
        )
