from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={
                                   'placeholder': 'Type your comment here...',
                                   'class': "form-control",
                                   'rows': 1
                              }),
                              label='')

    class Meta:
        model = Comments
        fields = ['content']


