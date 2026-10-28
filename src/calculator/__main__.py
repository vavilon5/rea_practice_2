"""Точка входа командной строки: ``python -m calculator "2 + 3"``."""

import sys

from calculator.expression import evaluate


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print('Использование: python -m calculator "<a> <op> <b>"', file=sys.stderr)
        return 2
    try:
        print(evaluate(args[0]))
    except (ValueError, ZeroDivisionError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
