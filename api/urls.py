from django.urls import path

from .views.category import CategoryView, CategoryDetailsView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:id>', CategoryDetailsView.as_view(), name='category-details'),
]
