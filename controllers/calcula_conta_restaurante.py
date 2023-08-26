from typing import NewType, Union

ValorContaDoRestaurante = NewType("ValorContaDoRestaurante", float)
ValorGorjetaDoRestaurante = NewType("ValorGorjetaDoRestaurante", float)


def calcular_conta_restaurante(valor_despesa: "ValorDespesa") -> Union[ValorContaDoRestaurante, ValorGorjetaDoRestaurante]:
    comissao = 0.10 * valor_despesa.valor_despesa
    valor_total = valor_despesa.valor_despesa + comissao
    valor_gorjeta = comissao
    return round(valor_total, 2), round(valor_gorjeta, 2)
