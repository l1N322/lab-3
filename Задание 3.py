#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == "__main__":
    k = int(input("Введите число: "))

    if k < 2:
        print(0)
    else:
        simple = 1
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                simple = 0
                break
        print(simple)