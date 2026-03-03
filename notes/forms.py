from django import forms

from notes.models import Note, Category


class CreateNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Título',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Conteúdo',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.filter(user=user)


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Nome',
            }),
        }
