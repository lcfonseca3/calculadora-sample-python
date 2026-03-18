"""
Interface de linha de comando da Calculadora de 8 Dígitos.
"""

from calculadora import somar, subtrair, multiplicar, dividir, formatar


def main():
    print("╔══════════════════════════════╗")
    print("║   Calculadora de 8 Dígitos   ║")
    print("╚══════════════════════════════╝")

    operacoes = {
        "1": ("Soma",           "+", somar),
        "2": ("Subtração",      "-", subtrair),
        "3": ("Multiplicação",  "×", multiplicar),
        "4": ("Divisão",        "÷", dividir),
    }

    while True:
        print("\nOperações disponíveis:")
        print("  1 → Soma        (+)")
        print("  2 → Subtração   (-)")
        print("  3 → Multiplicação (×)")
        print("  4 → Divisão     (÷)")
        print("  0 → Sair")

        opcao = input("\nEscolha a operação: ").strip()

        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao not in operacoes:
            print("Opção inválida! Digite um número de 0 a 4.")
            continue

        try:
            a = float(input("Digite o primeiro número: ").strip())
            b = float(input("Digite o segundo número: ").strip())
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")
            continue

        nome, simbolo, func = operacoes[opcao]

        try:
            resultado = func(a, b)
            print("┌─────────────────────────────┐")
            print(f"│  {a} {simbolo} {b} = {formatar(resultado)}")
            print("└─────────────────────────────┘")
        except (OverflowError, ZeroDivisionError) as e:
            print(f"⚠️  {e}")


if __name__ == "__main__":
    main()
