text_to_morse = dict()

with open('morse.txt', 'r') as fp:
    for line in fp:
        key, value = line.split()
        text_to_morse[key] = value
print(text_to_morse)

text_to_morse.setdefault('')

def convertToMorse(s: str) -> str:
    out_string: str = ''
    s.strip()
    for i in s:
        if i == ' ':
            out_string.append(' / ')
        else:
            out_string.append(text_to_morse.get(i))
    return out_string

