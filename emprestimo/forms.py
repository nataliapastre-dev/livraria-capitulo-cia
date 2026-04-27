from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmprestimoForm
from cadastro.models import Emprestimo
from datetime import date


def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_emprestimos')
            except Exception as e:
                form.add_error(None, e)
    else:
        form = EmprestimoForm()

    return render(request, 'emprestimo/emprestimo_form.html', {'form': form})


def devolver_livro(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)

    if emprestimo.data_devolucao is None:
        emprestimo.data_devolucao = date.today()
        emprestimo.save()

    return redirect('listar_emprestimos')