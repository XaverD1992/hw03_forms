from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {'group': 'Группа', 'text': 'Сообщение'}
        help_texts = {'group': 'Выберите группу', 'text': 'Введите ссообщение'}
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('А кто поле будет заполнять, Пушкин?')
        return data
