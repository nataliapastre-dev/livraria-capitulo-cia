from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Livro  # Certifique-se que o app 'cadastro' tem o modelo Livro

class Emprestimo(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.PROTECT,
        related_name="emprestimos_emprestimo"  # nome único para evitar conflito
    )

    # QUEM RECEBEU O LIVRO (pessoa de fora)
    nome_pessoa = models.CharField(max_length=100)

    # QUEM FEZ O REGISTRO (usuário logado)
    registrado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    # Datas
    data_emprestimo = models.DateField(auto_now_add=True)
    previsao_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    # Multa, caso haja atraso
    valor_multa = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nome_pessoa} - {self.livro.titulo}"