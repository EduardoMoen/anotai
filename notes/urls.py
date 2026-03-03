from django.urls import path
from .views import notes_list, categories_list, create_notes, create_category, delete_notes, update_notes, \
    delete_category, update_category

urlpatterns = [
    path('', notes_list, name='notes_list'),
    path('create/', create_notes, name='create_notes'),
    path('delete/<int:pk>/', delete_notes, name='delete_notes'),
    path('update/<int:pk>/', update_notes, name='update_notes'),
    path('categories/', categories_list, name='categories_list'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/<int:pk>/', update_category, name='update_category'),
    path('categories/delete/<int:pk>/', delete_category, name='delete_category'),
]

app_name = 'notes'
