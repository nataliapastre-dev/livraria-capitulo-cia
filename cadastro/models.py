from django.contrib.auth.models import User
from django.db import models


# Modelo Autor
class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Modelo Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Modelo Editora
class Editora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Modelo Livro
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    # ✔ ajustado para evitar erro de migration
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    ano_publicacao = models.PositiveIntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)

    codigo = models.PositiveIntegerField(unique=True)

    quantidade_total = models.PositiveIntegerField()
    quantidade_disponivel = models.PositiveIntegerField()

    localizacao = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)

    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)

    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"


# Modelo Usuario
class Usuario(models.Model):
    TIPO_USUARIO = (
        ("A", "Administrador"),
        ("L", "Leitor"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    numero_carterinha = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO, default="L")

    def __str__(self):
        return self.user.username


# Modelo Emprestimo
class Emprestimo(models.Model):
    STATUS = (
        ("E", "Emprestado"),
        ("D", "Devolvido"),
        ("A", "Atrasado"),
    )

    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    data_emprestimo = models.DateField(auto_now_add=True)
    previsao_devolucao = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)

    valor_multa = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS, default="E")

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.livro.quantidade_disponivel > 0:
                self.livro.quantidade_disponivel -= 1
                self.livro.save()
            else:
                raise ValueError("Livro indisponível")
        super().save(*args, **kwargs)

    def devolver(self):
        from datetime import date

        if not self.data_devolucao:
            self.data_devolucao = date.today()
            self.status = "D"

            self.livro.quantidade_disponivel += 1
            self.livro.save()

            self.save()

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario}"