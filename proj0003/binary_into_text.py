binary = "01001000 01100101 01101100 01101100 01101111 "
text = ''

for i in binary.split():
    text += ''.join(chr(int(i, 2)))

print(text)