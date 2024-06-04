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
