import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

message = ""
for col in range(0, m):
    for row in matrix:
        word = row[col]
        for ch in list(word):
            message += ((ch.isspace() or ch.isalnum() or ch in ('', '!', '@', '#', '%', '$', '&')) and ch) or " "

decoded_script = ""
for character in message:
    decoded_script += (character not in ('!', '@', '#', '$', '%', '&') and character) or " "
decoded_script = re.sub(' +', ' ', decoded_script)

decoded_script = list(decoded_script)
decoded_script[0] = (not decoded_script[0].isspace() and decoded_script[0]) or ""
line = ""

decoded_script = list(decoded_script)
decoded_script[-1] = (not decoded_script[-1].isspace() and decoded_script[-1]) or ""
line = ""

for i in decoded_script:
    line += i
alphnum = line

symbols = ""
for ch in list(message):
    symbols += (not ch.isalnum() and ch) or "."
tail = symbols.split(".")[-1]
head = symbols.split(".")[0]

decoded_script = (not alphnum.isalnum() and ((tail != head and head + alphnum + tail) or head)) or alphnum

print(decoded_script, end="\n")