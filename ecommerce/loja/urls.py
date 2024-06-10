from django.urls import path
from .views import *
from django.views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('', view=homepage, name='homepage'),
    path('loja/', view=loja, name='loja'),
    path('loja/<str:filtro>/', view=loja, name='loja'),
    path('produto/<int:id_produto>/', view=ver_produto, name='ver_produto'),
    path('produto/<int:id_produto>/<int:id_cor>', view=ver_produto, name='ver_produto'),
    path('carrinho/', view=carrinho, name='carrinho'),
    path('checkout/', view=checkout, name='checkout'),
    path('finalizarpedido/<int:id_pedido>/', view=finalizar_pedido, name='finalizar_pedido'),
    path('finalizarpagamento', view=finalizar_pagamento, name='finalizar_pagamento'),
    path('adicionarcarrinho/<int:id_produto>/', view=adicionar_carrinho, name='adicionar_carrinho'),
    path('removercarrinho/<int:id_produto>/', view=remover_carrinho, name='remover_carrinho'),
    path('adicionarendereco/', view=adicionar_endereco, name='adicionar_endereco'),

    path('minhaconta/', view=minha_conta, name='minha_conta'),
    path('meuspedidos/', view=meus_pedidos, name='meus_pedidos'),
    path('pedidoaprovado/<int:id_pedido>', view=pedido_aprovado, name='pedido_aprovado'),
    path('fazerlogin/', view=fazer_login, name='fazer_login'),
    path('fazerlogout/', view=fazer_logout, name='fazer_logout'),
    path('criarconta/', view=criar_conta, name='criar_conta'),

    path("gerenciarloja", gerenciar_loja, name="gerenciar_loja"),
    path("exportarrelatorio/<str:relatorio>/", exportar_relatorio, name="exportar_relatorio"),

    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    


]