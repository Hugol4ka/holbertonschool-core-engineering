#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for i in range(len(ligne)):
            print("{:d}".format(ligne[i]), end="")
            if i < len(ligne) - 1:
                print(" ", end="")
        print()
