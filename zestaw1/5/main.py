first_set = {2.0, 5, 5, "Set", (2, 3, 4)}
second_set = {3.0, 5, 7.0, "Set", "set", (2, 3, 4)}

print("The first set: ", first_set, "\n", "The second set: ", second_set, sep="")
print("\n")

union = first_set | second_set
intersection = first_set & second_set

print("The intersection:", intersection)
print("The union: ", union)
