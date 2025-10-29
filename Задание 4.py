#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10


if __name__ == "__main__":
    x = float(input("Введите x (0 <= x <= 2): "))

    # Если x = 1, то все члены ряда равны 0.
    if x == 1:
        print("f(1) = 0")
    elif x < 0 or x > 2:
        print("Некорректное значение x", file=sys.stderr)
        exit(1)
    else:
        total = 0
        k = 1

        while True:
            value = (-1)**k * (x - 1)**k / (k * k)
            total += value
            if math.fabs(value) < EPS:
                break
            k += 1

        print(f"f({x}) = {total}")