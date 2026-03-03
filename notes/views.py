from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import CreateNotesForm, CreateCategoryForm, SearchTitleNotesForm


@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    search = SearchTitleNotesForm(request.GET)

    if search.is_valid():
        title = search.cleaned_data['title']
        if title:
            notes = notes.filter(title__icontains=title)

    return render(request, 'notes/notes_list.html', {
        'notes': notes,
        'search': search
    })

@login_required
def create_notes(request):
    if request.method == 'POST':
        form = CreateNotesForm(request.POST, user=request.user)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
            return redirect('notes:notes_list')

    else:
        form = CreateNotesForm(user=request.user)

    return render(request, 'notes/notes_form.html', {
        'form': form
    })

@login_required
def update_notes(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CreateNotesForm(request.POST, user=request.user, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
            return redirect('notes:notes_list')

    else:
        form = CreateNotesForm(user=request.user, instance=note)

    return render(request, 'notes/notes_form.html', {
        'note': note,
        'form': form,
    })

@login_required
def delete_notes(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        note.delete()
        return redirect('notes:notes_list')

    return render(request, 'notes/delete_notes.html', {
        'note': note
    })

@login_required
def categories_list(request):
    categories = Category.objects.filter(user=request.user)

    return render(request, 'notes/categories_list.html',{
        'categories': categories
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            form.save()
            return redirect('notes:categories_list')

    else:
        form = CreateCategoryForm()

    return render(request, 'notes/category_form.html', {
        'form': form
    })

def update_category(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk,
        user=request.user,
    )

    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            form.save()
            return redirect('notes:categories_list')

    else:
        form = CreateCategoryForm(instance=category)

    return render(request, 'notes/category_form.html', {
        'form': form,
        'category': category
    })

def delete_category(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk,
        user=request.user,
    )

    if request.method == 'POST':
        category.delete()
        return redirect('notes:categories_list')

    return render(request, 'notes/delete_category.html', {
        'category': category
    })
