from django.db.models import Max, Min

def filtrar_produtos(produtos, filtro):
    if filtro:
        if "-" in filtro:
            categoria, tipo = filtro.split("-")
            produtos = produtos.filter(tipo__slug=tipo, categoria__slug=categoria)
        else:
            produtos = produtos.filter(categoria__slug=filtro)
    return produtos


def preco_minimo_maximo(produtos):
    minimo = 0
    maximo = 0
    if len(produtos) > 0:
        # encontra o maximo e minino
        minimo = list(produtos.aggregate(Min('preco')).values())[0]
        maximo = list(produtos.aggregate(Max('preco')).values())[0]
        # arredonda para 2 casas decimais
        minimo = round(minimo, 2)
        maximo = round(maximo, 2)
    return minimo, maximo


def ordenar_produtos(produtos, ordem):
    if ordem == "menor-preco":
        produtos = produtos.order_by("preco")
    elif ordem == "maior-preco":
        produtos = produtos.order_by("-preco")
    elif ordem == "mais-vendidos":
        lista_produtos = [(produto.total_vendas(), produto) for produto in produtos]
        lista_produtos = sorted(lista_produtos, key=lambda item: item[0], reverse=True)
        produtos = [item[1] for item in lista_produtos]
    return produtos
