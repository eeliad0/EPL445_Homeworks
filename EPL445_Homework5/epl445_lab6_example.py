from Huffman3 import huffman, encode, decode, makenodes, iterate
import collections
import numpy as np

myList = [1, 2, 3, 4, 3, 2, 2, 1, 1, 1]
print("myList: ", myList)

# Find frequency of appearance for each value of the list
counter = collections.Counter(myList)

# Define list of probabilities as list of pairs (Unique item, Corresponding frequency)
probs = []

# Initialization of probabilities' list
for key, value in counter.items():
    print(key, value)
    probs.append((key, np.float32(value)))

# Creates a list of nodes ready for the Huffman algorithm 'iterate'.
symbols = makenodes(probs)

# Runs the Huffman algorithm on a list of "nodes". It returns a pointer to the root of a new tree of "internal nodes".
root = iterate(symbols)

# Encodes a list of source symbols.
s = encode(myList, symbols)
print("Huffman encoding of myList: ", s)


# Decodes a binary string using the Huffman tree accessed via root
d = decode(s, root)
print("Huffman decoding of myList: ", d)

