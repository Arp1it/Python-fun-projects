def text_to_binary(text):
    binary = ''

    for i in text:
        binary += format(ord(i), '08b') + ' '

    return binary

def binary_to_text(binary):
    text = ''

    for i in binary.split():
        text += chr(int(i, 2))

    return text

text = "Hello"

binry = text_to_binary(text=text)
print(binry)
print(binary_to_text(binry))