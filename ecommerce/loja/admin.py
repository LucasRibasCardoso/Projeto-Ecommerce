from django.contrib import admin
from .models import *

admin.site.register(Cliente),
admin.site.register(Categoria),
admin.site.register(Tipo),
admin.site.register(Produto),
admin.site.register(Endereco),
admin.site.register(ItemEstoque),
admin.site.register(Pedido),
admin.site.register(ItemPedido),
admin.site.register(Banner),
admin.site.register(Cor)
