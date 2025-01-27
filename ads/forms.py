from django import forms
from .models import Ad , Comment , Tag

class AdForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'tags', 'image']

image = forms.ImageField(required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



