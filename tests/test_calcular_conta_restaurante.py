from dataclasses import dataclass
from typing import Union

import pytest
from dataclass_type_validator import dataclass_validate

from controllers.calcula_conta_restaurante import calcular_conta_restaurante


@dataclass_validate
@dataclass
class ValorDespesa:
    valor_despesa: Union[int, float]


def test_calcular_conta_restaurante():
    valor_despesa = ValorDespesa(
        valor_despesa=75.00,
    )
    valor_total_esperado = 82.50
    valor_gorjeta_esperado = 7.50
    assert calcular_conta_restaurante(valor_despesa) == (valor_total_esperado, valor_gorjeta_esperado)

    valor_despesa = ValorDespesa(
        valor_despesa=125.00,
    )
    valor_total_esperado = 137.50
    valor_gorjeta_esperado = 12.50
    assert calcular_conta_restaurante(valor_despesa) == (valor_total_esperado, valor_gorjeta_esperado)

    valor_despesa = ValorDespesa(
        valor_despesa=350.87,
    )
    valor_total_esperado = 385.96
    valor_gorjeta_esperado = 35.09
    assert calcular_conta_restaurante(valor_despesa) == (valor_total_esperado, valor_gorjeta_esperado)


if __name__ == '__main__':
    pytest.main()
