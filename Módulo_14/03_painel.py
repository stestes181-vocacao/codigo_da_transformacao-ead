from django.contrib import admin
from .models import Produto

admin.site.register(Produto)

from django.test import TestCase
from .models import Produto

class ProdutoTest(TestCase):
    def test_produto(self):
        produto = Produto.objects.create(
            nome='Mouse',
            descricao='Mouse Gamer',
            preco=100,
            quantidade=5
        )

        self.assertEqual(produto.nome, 'Mouse')