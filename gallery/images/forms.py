# -*- coding: utf-8 -*-
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'pic',
            'text',
        ]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['pic'].label = ''
        self.fields['text'].label = ''
