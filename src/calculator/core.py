"""Базовые арифметические операции."""

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Возвращает сумму ``a`` и ``b``."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Возвращает разность ``a`` и ``b``."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Возвращает произведение ``a`` и ``b``."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Возвращает частное ``a / b``.

    Raises:
        ZeroDivisionError: если ``b`` равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b
