"""Вычисление простых выражений вида ``"<число> <оператор> <число>"``."""

from calculator.core import Number, add, divide, modulo, multiply, power, subtract

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "^": power,
}


def _parse_number(token: str) -> Number:
    try:
        return int(token)
    except ValueError:
        return float(token)


def evaluate(expression: str) -> Number:
    """Вычисляет выражение из двух операндов и одного оператора.

    >>> evaluate("2 + 3")
    5

    Raises:
        ValueError: если выражение имеет неверный формат или оператор.
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError(f"Неверный формат выражения: {expression!r}")
    left, op, right = parts
    if op not in OPERATIONS:
        raise ValueError(f"Неизвестный оператор: {op!r}")
    return OPERATIONS[op](_parse_number(left), _parse_number(right))
