from django.contrib import admin
from django.utils.html import mark_safe
from .models import Editora, Livro, Usuario, Emprestimo, Autor


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'editora', 'preco', 'preview')

    def preview(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" width="60" />')
        return "Sem imagem"

    preview.short_description = "Capa"

    readonly_fields = ('preview_form',)

    fieldsets = (
        ('Dados do Livro', {
            'fields': (
                'titulo',
                'descricao',
                'autor',  # 👈 ADICIONADO AQUI
                'preco',
                'ano_publicacao',
                'editora',
                'codigo',
                'quantidade_total',
                'quantidade_disponivel',
                'localizacao',
                'idioma'
            )
        }),
        ('Imagem do Livro', {
            'fields': ('imagem', 'preview_form'),
        }),
    )

    def preview_form(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" width="150" />')
        return "Nenhuma imagem enviada"

    preview_form.short_description = "Prévia da capa"


admin.site.register(Editora)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
admin.site.register(Autor)