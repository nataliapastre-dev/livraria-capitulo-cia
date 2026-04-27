from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # 📚 LISTA DE LIVROS (FALTANDO)
    path('livros/', views.lista_livros, name='lista_livros'),

    path('livro/<int:id>/', views.detalhe_livro, name='detalhe_livro'),
]