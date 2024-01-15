from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(attrs={
                               'placeholder': 'Type your comment here...',
                               'class': "form-control"
                           }),
                           label='')

    class Meta:
        model = Comments
        fields = ['content']


