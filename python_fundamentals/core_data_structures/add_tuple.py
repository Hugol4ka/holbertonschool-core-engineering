#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)

    somme_1 = new_a[0] + new_b[0]
    somme_2 = new_a[1] + new_b[1]

    return (somme_1, somme_2)
