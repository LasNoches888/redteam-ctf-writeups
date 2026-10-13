#!/usr/bin/env python3
"""Генератор учебного задания «XOR одним байтом».

Задание самодельное: ключ и флаг зафиксированы, чтобы результат был воспроизводимым.
Запуск:  python make_challenge.py > challenge.hex
"""

PLAINTEXT = b"The quick brown fox jumps over the lazy dog. flag{demo_single_byte_xor}"
KEY = 0x5A


def encrypt(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)


if __name__ == "__main__":
    print(encrypt(PLAINTEXT, KEY).hex())
