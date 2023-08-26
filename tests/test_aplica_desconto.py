from dataclasses import dataclass
from typing import Union

import pytest
from dataclass_type_validator import dataclass_validate

from controllers.aplica_desconto import aplicar_desconto


@dataclass_validate
@dataclass
class ValorProdutoDesconto:
    valor_produto: Union[int, float]
    desconto_percentual: Union[int, float]


def test_aplicar_desconto():
    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=100,
        desconto_percentual=9,
    )
    novo_valor_esperado = 91.00
    assert aplicar_desconto(valor_produto_desconto) == novo_valor_esperado

    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=1500,
        desconto_percentual=9,
    )
    novo_valor_esperado = 1365.00
    assert aplicar_desconto(valor_produto_desconto) == novo_valor_esperado

    valor_produto_desconto = ValorProdutoDesconto(
        valor_produto=60000,
        desconto_percentual=9,
    )
    novo_valor_esperado = 54600.00
    assert aplicar_desconto(valor_produto_desconto) == novo_valor_esperado


if __name__ == '__main__':
    pytest.main()
