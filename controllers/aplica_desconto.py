from typing import NewType

ValorComDesconto = NewType("ValorComDesconto", float)


def aplicar_desconto(valor_produto_desconto: "ValorProdutoDesconto") -> ValorComDesconto:
    desconto = (valor_produto_desconto.desconto_percentual / 100) * valor_produto_desconto.valor_produto
    novo_valor = valor_produto_desconto.valor_produto - desconto
    return round(novo_valor, 2)
