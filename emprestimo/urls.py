from django.urls import path
from . import views

urlpatterns = [
    path('emprestar/', views.criar_emprestimo, name='criar_emprestimo'),
    path('devolver/<int:id>/', views.devolver_livro, name='devolver_livro'),
]