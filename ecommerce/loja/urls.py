from django.urls import path
from .views import *

urlpatterns = [
    path('', view=homepage, name='homepage'),
    path('loja/', view=loja, name='loja'),
    path('loja/<str:filtro>/', view=loja, name='loja'),
    path('produto/<int:id_produto>/', view=ver_produto, name='ver_produto'),
    path('produto/<int:id_produto>/<int:id_cor>', view=ver_produto, name='ver_produto'),
    path('carrinho/', view=carrinho, name='carrinho'),
    path('checkout/', view=checkout, name='checkout'),
    path('minhaconta/', view=minhaconta, name='minhaconta'),
    path('login/', view=login, name='login'),
    path('adicionarcarrinho/<int:id_produto>/', view=adicionar_carrinho, name='adicionar_carrinho'),
    path('removercarrinho/<int:id_produto>/', view=remover_carrinho, name='remover_carrinho'),
    path('adicionarendereco/', view=adicionar_endereco, name='adicionar_endereco'),

]