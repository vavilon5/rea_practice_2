"""Calculator — учебный проект для практической работы по CI/CD.

Пакет предоставляет базовые арифметические операции и простой
вычислитель выражений вида ``"2 + 3"``.
"""

from calculator.core import add, divide, multiply, subtract
from calculator.expression import evaluate

__version__ = "1.0.0"

__all__ = ["add", "subtract", "multiply", "divide", "evaluate", "__version__"]
