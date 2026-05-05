#!/usr/bin/env python3

result = ""
for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
    if letter != 'q' and letter != 'e':
        result += letter
print("{}".format(result), end="")
