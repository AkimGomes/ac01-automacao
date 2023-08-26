from dataclasses import dataclass
from typing import Union

import pytest
from dataclass_type_validator import dataclass_validate

from controllers.calcula_promocao import calcular_valor_promocao


@dataclass_validate
@dataclass
class ValorDescontoProduto:
    valor_original: Union[int, float]
    desconto: Union[int, float]


def test_calcular_valor_promocao():
    valor_desconto = ValorDescontoProduto(
        valor_original=500.00,
        desconto=50.00,
    )
    valor_promocao_esperado = 450.00
    assert calcular_valor_promocao(valor_desconto) == valor_promocao_esperado

    valor_desconto = ValorDescontoProduto(
        valor_original=10500.00,
        desconto=500.00,
    )
    valor_promocao_esperado = 10000.00
    assert calcular_valor_promocao(valor_desconto) == valor_promocao_esperado

    valor_desconto = ValorDescontoProduto(
        valor_original=90.00,
        desconto=0.80,
    )
    valor_promocao_esperado = 89.20
    assert calcular_valor_promocao(valor_desconto) == valor_promocao_esperado


if __name__ == '__main__':
    pytest.main()
