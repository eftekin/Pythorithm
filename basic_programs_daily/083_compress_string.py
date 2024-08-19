# Write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!".

import zlib

string = "hello world!hello world!hello world!hello world!"

# Compress the String
compressed_string = zlib.compress(string.encode())

# Decompress the string
decompressed_string = zlib.decompress(compressed_string).decode()

print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
