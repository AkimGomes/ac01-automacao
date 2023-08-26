from dataclasses import dataclass
from typing import NewType, Union
from dataclass_type_validator import dataclass_validate

SalarioLiquido = NewType("SalarioLiquido", float)


@dataclass_validate
@dataclass
class CasoDeGanhos:
    valor_hora_aula: Union[int, float]
    numero_de_aulas: Union[int, float]
    percentual_inss: Union[int, float]

    def calcular_salario_liquido(self) -> SalarioLiquido:
        salario_bruto = self.valor_hora_aula * self.numero_de_aulas
        desconto_inss = (self.percentual_inss / 100) * salario_bruto
        salario_liquido = salario_bruto - desconto_inss
        return round(salario_liquido, 2)
