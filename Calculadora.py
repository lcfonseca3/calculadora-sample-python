"""
Calculadora simples de 8 dígitos.
Suporta operações básicas: soma, subtração, multiplicação e divisão.
"""

MAX_VALOR = 99999999
MIN_VALOR = -9999999


def validar(valor: float) -> None:
    """Valida se o resultado está dentro do limite de 8 dígitos."""
    if valor > MAX_VALOR or valor < MIN_VALOR:
        raise OverflowError("Erro: Resultado excede o limite de 8 dígitos.")


def formatar(valor: float) -> str:
    """Formata o resultado para exibição."""
    validar(valor)
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.8g}"


def somar(a: float, b: float) -> float:
    resultado = a + b
    validar(resultado)
    return resultado


def subtrair(a: float, b: float) -> float:
    resultado = a - b
    validar(resultado)
    return resultado


def multiplicar(a: float, b: float) -> float:
    resultado = a * b
    validar(resultado)
    return resultado


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    resultado = a / b
    validar(resultado)
    return resultado
