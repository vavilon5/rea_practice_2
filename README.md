# rea_practice_2 — Calculator

ПЗ 2: настройка CI/CD с помощью GitHub Actions на примере небольшого Python-проекта.

[![CI](https://github.com/vavilon5/rea_practice_2/actions/workflows/main.yml/badge.svg)](https://github.com/vavilon5/rea_practice_2/actions/workflows/main.yml)
[![Docs](https://github.com/vavilon5/rea_practice_2/actions/workflows/docs.yml/badge.svg)](https://github.com/vavilon5/rea_practice_2/actions/workflows/docs.yml)

## Установка и запуск

```bash
pip install -e . -r requirements-dev.txt
python -m calculator "2 + 3"
```

## Тесты

```bash
pytest
```

## Документация

- Руководство: [docs/usage.md](docs/usage.md), процесс CI/CD: [docs/ci-cd.md](docs/ci-cd.md)
- API-документация генерируется `pdoc` в CI и публикуется в ветку `gh-pages`.
- Отчёт по практической работе: [docs/REPORT.md](docs/REPORT.md)
