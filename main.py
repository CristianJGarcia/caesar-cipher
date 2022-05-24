def caesar_cipher(string, offset):
    # Write your code here.
    lst = []

    for letter in string:
        new_offset = ord(letter) - offset

        if new_offset < ord('a'):
            new_offset = (ord(letter) + 26) - offset
        lst.append(chr(new_offset))

    return "".join(lst)

print(caesar_cipher("hello", 3))