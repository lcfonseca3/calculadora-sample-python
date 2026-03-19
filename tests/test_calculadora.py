"""
Testes unitários para a Calculadora de 8 Dígitos.
"""

import pytest
from calculadora import somar, subtrair, multiplicar, dividir, formatar


# ── Soma ──────────────────────────────────────────────
def test_somar_positivos():
    assert somar(3, 7) == 10

def test_somar_negativos():
    assert somar(-3, -2) == -5

def test_somar_com_zero():
    assert somar(42, 0) == 42


# ── Subtração ─────────────────────────────────────────
def test_subtrair_positivos():
    assert subtrair(10, 7) == 3

def test_subtrair_resultado_negativo():
    assert subtrair(1, 5) == -4


# ── Multiplicação ─────────────────────────────────────
def test_multiplicar_positivos():
    assert multiplicar(4, 5) == 20

def test_multiplicar_por_zero():
    assert multiplicar(999, 0) == 0

def test_multiplicar_negativos():
    assert multiplicar(-2, -3) == 6


# ── Divisão ───────────────────────────────────────────
def test_dividir_exato():
    assert dividir(20, 5) == 4

def test_dividir_fracionado():
    assert dividir(5, 2) == 2.5

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)


# ── Limite de 8 dígitos ───────────────────────────────
def test_resultado_acima_do_limite():
    with pytest.raises(OverflowError):
        somar(99999999, 1)

def test_resultado_no_limite_maximo():
    assert somar(99999998, 1) == 99999999

def test_formatar_inteiro():
    assert formatar(42.0) == "42"

def test_formatar_decimal():
    assert formatar(2.5) == "2.5"
