# Индекс разборов

| Задание | Категория | Очки | Сложность | Разбор | Исходники |
|---------|-----------|------|-----------|--------|-----------|
| Login Bypass | web | 100 | лёгкая | [example_web_sqli.md](writeups/example_web_sqli.md) | — |
| Reflected XSS в поиске | web | 100 | лёгкая | [example_web_reflected_xss.md](writeups/example_web_reflected_xss.md) | [redteam-vulnerable-webapp-lab](https://github.com/LasNoches888/redteam-vulnerable-webapp-lab) |
| XOR одним байтом | crypto | 100 | лёгкая | [example_crypto_single_byte_xor.md](writeups/example_crypto_single_byte_xor.md) | [challenges/single_byte_xor](challenges/single_byte_xor) |

Новый разбор оформляйте по шаблону [`TEMPLATE.md`](TEMPLATE.md) и добавляйте строку в эту таблицу.
Подход к решению описан в [`docs/methodology.md`](docs/methodology.md), инструменты — в [`docs/tools.md`](docs/tools.md).

## Проверка учебных заданий
```bash
python -m unittest discover -s tests
```
