from django.forms import ModelForm
from .models import *
from tinymce.widgets import TinyMCE
from django import forms

class DiaryForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(id = user.id)
        self.fields['author'].initial = user

    class Meta:
        model = Diary
        fields = '__all__'

class ChapterForm(ModelForm):
    content = forms.CharField(widget = TinyMCE(attrs={'cols': 80, 'rows': 30}))

    def __init__(self, user, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.fields['diary'].queryset = Diary.objects.filter(author = user)

    class Meta:
        model = Chapter
        fields = '__all__'        
      