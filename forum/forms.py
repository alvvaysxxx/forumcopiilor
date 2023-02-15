from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'img']
        widgets = {
            'date': forms.HiddenInput(),
            'image': forms.ClearableFileInput(attrs={'clearable': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].required = False
        self.fields['img'].widget.template_with_initial = False

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comments',)
