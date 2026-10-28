"""Calculator — учебный проект для практической работы по CI/CD.

Пакет предоставляет базовые арифметические операции и простой
вычислитель выражений вида ``"2 + 3"``.
"""

from calculator.core import add, divide, modulo, multiply, power, subtract
from calculator.expression import evaluate

__version__ = "1.1.0"

__all__ = ["add", "subtract", "multiply", "divide", "power", "modulo", "evaluate", "__version__"]
