import numpy as np
x = np.random.choice(6, size=5)
print(x)
x = 1 + np.random.choice(6, size=(2,4))
print(x)
nucleotides = ["A", "G", "C", "T"]
dna = np.random.choice(nucleotides, 5)
print("".join(dna))