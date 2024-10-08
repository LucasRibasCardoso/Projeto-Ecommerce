from .models import Pedido, ItemPedido, Cliente, Categoria, Tipo


def carrinho(request):
    quantidade_produtos_carrinho = 0

    if request.user.is_authenticated:
        cliente = request.user.cliente
    else:
        # pega o cliente que nao fez login, gerando um id da sessao e adicionando nos cookies do navegador
        if request.COOKIES.get('id_sessao'):
            id_sessao = request.COOKIES.get('id_sessao')
            cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
        else:
            return {'quantidade_produtos_carrinho': quantidade_produtos_carrinho} 

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItemPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_produtos_carrinho += item.quantidade
    return {'quantidade_produtos_carrinho': quantidade_produtos_carrinho} 


def categorias_tipos(request):
    categorias_navegacao = Categoria.objects.all()
    tipos_navegacao = Tipo.objects.all()
    return {"categorias_navegacao": categorias_navegacao, "tipos_navegacao": tipos_navegacao}

def faz_parte_equipe(request):
    equipe = False
    if request.user.is_authenticated:
        # verifica se existe um grupo associado a esse user
        if request.user.groups.filter(name='equipe').exists():
            equipe = True
    return {"equipe": equipe}            
