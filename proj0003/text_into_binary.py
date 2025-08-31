text = "Hello"
binary = ''

for i in text:
    binary += format(ord(i), '08b')+' '

print(binary)