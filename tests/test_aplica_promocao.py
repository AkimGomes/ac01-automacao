import pytest
from models.calcula_promocao import ValorDescontoProduto


def test_calcular_valor_promocao():
    valor_desconto = ValorDescontoProduto(
        valor_original=500.00,
        desconto=50.00,
    )
    valor_promocao_esperado = 450.00
    assert valor_desconto.calcular_valor_promocao() == valor_promocao_esperado

    valor_desconto = ValorDescontoProduto(
        valor_original=10500.00,
        desconto=500.00,
    )
    valor_promocao_esperado = 10000.00
    assert valor_desconto.calcular_valor_promocao() == valor_promocao_esperado

    valor_desconto = ValorDescontoProduto(
        valor_original=90.00,
        desconto=0.80,
    )
    valor_promocao_esperado = 89.20
    assert valor_desconto.calcular_valor_promocao() == valor_promocao_esperado


if __name__ == '__main__':
    pytest.main()
