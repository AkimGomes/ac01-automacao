import pytest
from models.calcula_conta_restaurante import ValorDespesa


def test_calcular_conta_restaurante():
    valor_despesa = ValorDespesa(
        valor_despesa=75.00,
    )
    valor_total_esperado = 82.50
    valor_gorjeta_esperado = 7.50
    assert valor_despesa.calcular_conta_restaurante() == (valor_total_esperado, valor_gorjeta_esperado)

    valor_despesa = ValorDespesa(
        valor_despesa=125.00,
    )
    valor_total_esperado = 137.50
    valor_gorjeta_esperado = 12.50
    assert valor_despesa.calcular_conta_restaurante() == (valor_total_esperado, valor_gorjeta_esperado)

    valor_despesa = ValorDespesa(
        valor_despesa=350.87,
    )
    valor_total_esperado = 385.96
    valor_gorjeta_esperado = 35.09
    assert valor_despesa.calcular_conta_restaurante() == (valor_total_esperado, valor_gorjeta_esperado)


if __name__ == '__main__':
    pytest.main()
