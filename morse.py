text_to_morse = dict()

with open('morse.txt', 'r') as fp:
    for line in fp:
        key, value = line.split()
        text_to_morse[key] = value
print(text_to_morse)


def convertToMorse(s):
    out_string = ''
    for i in s:
        pass
