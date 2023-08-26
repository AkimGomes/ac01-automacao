from dataclasses import dataclass
from typing import NewType, Union
from dataclass_type_validator import dataclass_validate

ValorComDesconto = NewType("ValorComDesconto", float)


@dataclass_validate
@dataclass
class ValorProdutoDesconto:
    valor_produto: Union[int, float]
    desconto_percentual: Union[int, float]

    def aplicar_desconto(self) -> ValorComDesconto:
        desconto = (self.desconto_percentual / 100) * self.valor_produto
        novo_valor = self.valor_produto - desconto
        return round(novo_valor, 2)
