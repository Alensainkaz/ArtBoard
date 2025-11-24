from django import forms

from .models import Pictures


class PictureForm(forms.ModelForm):
    class Meta:
        model=Pictures
        fields=['title','description','category','image']
