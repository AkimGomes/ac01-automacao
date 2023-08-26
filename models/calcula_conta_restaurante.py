from dataclasses import dataclass
from typing import NewType, Union

from dataclass_type_validator import dataclass_validate

ValorContaDoRestaurante = NewType("ValorContaDoRestaurante", float)
ValorGorjetaDoRestaurante = NewType("ValorGorjetaDoRestaurante", float)


@dataclass_validate
@dataclass
class ValorDespesa:
    valor_despesa: Union[int, float]

    def calcular_conta_restaurante(self) -> Union[ValorContaDoRestaurante, ValorGorjetaDoRestaurante]:
        comissao = 0.10 * self.valor_despesa
        valor_total = self.valor_despesa + comissao
        valor_gorjeta = comissao
        return round(valor_total, 2), round(valor_gorjeta, 2)
