from django.shortcuts import render, get_object_or_404
from .models import Livro


# 🔎 função reutilizável (evita repetição)
def filtrar_livros(request):
    busca = request.GET.get('busca')
    livros = Livro.objects.all()

    if busca:
        livros = livros.filter(titulo__icontains=busca)

    return livros


# 🏠 página inicial
def index(request):
    livros = filtrar_livros(request)

    return render(request, "index.html", {
        "livros": livros
    })


# 📚 página de livros
def lista_livros(request):
    livros = filtrar_livros(request)

    return render(request, "livros.html", {
        "livros": livros
    })


# 📖 detalhe do livro
def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    return render(request, "detalhe_livro.html", {
        "livro": livro
    })