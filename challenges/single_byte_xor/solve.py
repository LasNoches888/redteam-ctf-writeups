#!/usr/bin/env python3
"""Решение задания «XOR одним байтом»: перебор всех 256 ключей и оценка читаемости.

Использование:  python solve.py challenge.hex
"""
import sys

# Частые символы английского текста: пробел и буквы. Чем их больше, тем «читаемее» результат.
COMMON = set(b" etaoinshrdluETAOINSHRDLU")


def xor_with_key(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)


def score(candidate: bytes) -> int:
    """Оценка: +2 за частый символ, +1 за печатный ASCII, -5 за непечатный."""
    total = 0
    for b in candidate:
        if b in COMMON:
            total += 2
        elif 32 <= b < 127:
            total += 1
        else:
            total -= 5
    return total


def crack(ciphertext: bytes, top: int = 3) -> list[tuple[int, int, bytes]]:
    """Возвращает `top` лучших вариантов в виде (оценка, ключ, открытый текст)."""
    results = [(score(p := xor_with_key(ciphertext, k)), k, p) for k in range(256)]
    results.sort(reverse=True)
    return results[:top]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: solve.py <файл_с_hex>", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="ascii") as fh:
        ciphertext = bytes.fromhex(fh.read().strip())
    for points, key, plaintext in crack(ciphertext):
        print(f"ключ 0x{key:02x}  оценка {points:4d}  {plaintext.decode('latin-1')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
