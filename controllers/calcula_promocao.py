from typing import NewType

ValorComPromocao = NewType("ValorComPromocao", float)


def calcular_valor_promocao(valor_desconto: "ValorDescontoProduto") -> ValorComPromocao:
    valor_promocao = valor_desconto.valor_original - valor_desconto.desconto
    return round(valor_promocao, 2)
