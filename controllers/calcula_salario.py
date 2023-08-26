from typing import NewType

SalarioLiquido = NewType("SalarioLiquido", float)


def calcular_salario_liquido(caso_de_ganhos: "CasoDeGanhos") -> SalarioLiquido:
    salario_bruto = caso_de_ganhos.valor_hora_aula * caso_de_ganhos.numero_de_aulas
    desconto_inss = (caso_de_ganhos.percentual_inss / 100) * salario_bruto
    salario_liquido = salario_bruto - desconto_inss
    return round(salario_liquido, 2)
