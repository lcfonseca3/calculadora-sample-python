# 🧮 Calculadora de 8 Dígitos (Python)

Calculadora simples em Python com operações básicas e limite de 8 dígitos no resultado.

## ✨ Funcionalidades

- ➕ Soma
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- ⚠️ Validação de limite de 8 dígitos
- 🚫 Proteção contra divisão por zero
- 💻 Interface de linha de comando interativa

## 🚀 Como executar

### Pré-requisitos
- Python 3.8+

### Rodar a calculadora
```bash
python main.py
```

### Instalar dependências de teste
```bash
pip install -r requirements.txt
```

### Rodar os testes
```bash
pytest tests/
```

## 📁 Estrutura do projeto

```
calculadora-python/
├── calculadora.py        # Lógica da calculadora
├── main.py               # Interface CLI
├── requirements.txt      # Dependências
├── README.md
└── tests/
    └── test_calculadora.py  # Testes unitários (pytest)
```

## 🧪 Testes

O projeto inclui testes unitários com pytest cobrindo:
- Operações básicas (soma, subtração, multiplicação, divisão)
- Casos com zero e negativos
- Limite de 8 dígitos
- Exceções (divisão por zero, overflow)

## 📏 Regras da calculadora

| Condição | Comportamento |
|----------|--------------|
| Resultado > 99.999.999 | Lança `OverflowError` |
| Resultado < -9.999.999 | Lança `OverflowError` |
| Divisão por zero | Lança `ZeroDivisionError` |
