from dataclasses import dataclass
from typing import Union

import pytest
from dataclass_type_validator import dataclass_validate

from controllers.calcula_salario import calcular_salario_liquido


@dataclass_validate
@dataclass
class CasoDeGanhos:
    valor_hora_aula: Union[int, float]
    numero_de_aulas: Union[int, float]
    percentual_inss: Union[int, float]


def test_calculo_salario():
    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=6.25,
        numero_de_aulas=160,
        percentual_inss=1.3,
    )
    resultado_esperado = 987.00

    assert calcular_salario_liquido(caso_de_ganhos) == resultado_esperado

    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=20.5,
        numero_de_aulas=240,
        percentual_inss=1.7,
    )
    resultado_esperado = 4836.36
    assert calcular_salario_liquido(caso_de_ganhos) == resultado_esperado

    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=13.9,
        numero_de_aulas=200,
        percentual_inss=6.48,
    )
    resultado_esperado = 2599.86
    assert calcular_salario_liquido(caso_de_ganhos) == resultado_esperado


if __name__ == '__main__':
    pytest.main()
