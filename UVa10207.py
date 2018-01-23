#! /usr/bin/env python
# -*- utf-8 -*-
# code
# UVa10207
# edu001
# 2018/1/23
# 16:53
from functools import lru_cache
p = 0.5
q = 1 - p

@lru_cache()
def P(i, j):
    if i == 0:
        return 1
    elif j == 0:
        return 0
    else:
        # result = p(P(i,j)|P(i-1,j)) + p(P(i,j)|P(i,j-1)) = p * P(i - 1, j) + q * P(i, j - 1)
        return p * P(i - 1, j) + q * P(i, j - 1)


if __name__ == '__main__':
    print(P(5, 10))