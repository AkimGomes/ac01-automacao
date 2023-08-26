from dataclasses import dataclass
from typing import NewType, Union
from dataclass_type_validator import dataclass_validate

ValorComPromocao = NewType("ValorComPromocao", float)


@dataclass_validate
@dataclass
class ValorDescontoProduto:
    valor_original: Union[int, float]
    desconto: Union[int, float]

    def calcular_valor_promocao(self) -> ValorComPromocao:
        valor_promocao = self.valor_original - self.desconto
        return round(valor_promocao, 2)
