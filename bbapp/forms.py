from django import forms
from .models import CommentModel

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        exclude = ('target', 'pub_date')
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'コメント'}
            )
        }
