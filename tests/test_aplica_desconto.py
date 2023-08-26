import pytest

from models.aplica_desconto import ValorProdutoDesconto


def test_aplicar_desconto():
    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=100,
        desconto_percentual=9,
    )
    novo_valor_esperado = 91.00
    assert valor_produto_desconto.aplicar_desconto() == novo_valor_esperado

    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=1500,
        desconto_percentual=9,
    )
    novo_valor_esperado = 1365.00
    assert valor_produto_desconto.aplicar_desconto() == novo_valor_esperado

    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=60000,
        desconto_percentual=9,
    )
    novo_valor_esperado = 54600.00
    assert valor_produto_desconto.aplicar_desconto() == novo_valor_esperado


if __name__ == '__main__':
    pytest.main()
