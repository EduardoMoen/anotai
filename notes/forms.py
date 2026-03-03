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


class SearchTitleNotesForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Procurar por titulo de nota',
        })
    )


class SearchNameCategoryForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Procurar por nome',
        })
    )


class SearchCategoryNotesForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        empty_label="Procurar por categoria",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.filter(user=user)
