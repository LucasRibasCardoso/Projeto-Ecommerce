import mercadopago

public_key = "TEST-74d7b60a-a428-4b9e-95c4-88eb83b80d27"
token = "TEST-264048933700828-060820-7458e7197cc11665ac030dc08fabb3b0-1500010953"

def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    itens = []
    for item in itens_pedido:
        nome = item.item_estoque.produto.nome
        quantidade = int(item.quantidade)
        preco = float(item.item_estoque.produto.preco)
        itens.append({
            'title': nome,
            'quantity': quantidade,
            'unit_price': preco
        })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls":{
            'success': link,
            'pending': link,
            'failure': link
        }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    print(link_pagamento)
    return link_pagamento, id_pagamento
