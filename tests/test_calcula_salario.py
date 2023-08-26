import pytest
from models.calcula_salario import CasoDeGanhos


def test_calculo_salario():
    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=6.25,
        numero_de_aulas=160,
        percentual_inss=1.3,
    )
    resultado_esperado = 987.00

    assert caso_de_ganhos.calcular_salario_liquido() == resultado_esperado

    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=20.5,
        numero_de_aulas=240,
        percentual_inss=1.7,
    )
    resultado_esperado = 4836.36
    assert caso_de_ganhos.calcular_salario_liquido() == resultado_esperado

    caso_de_ganhos = CasoDeGanhos(
        valor_hora_aula=13.9,
        numero_de_aulas=200,
        percentual_inss=6.48,
    )
    resultado_esperado = 2599.86
    assert caso_de_ganhos.calcular_salario_liquido() == resultado_esperado


if __name__ == '__main__':
    pytest.main()
