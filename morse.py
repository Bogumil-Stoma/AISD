import argparse

text_to_morse = dict()

with open('morse.txt', 'r') as fp:
    for line in fp:
        key, value = line.split()
        text_to_morse[key] = value
print(text_to_morse)

#text_to_morse.setdefault('')

def convertToMorse(s: str) -> str:
    out_string: str = ''
    s.strip()
    for i in s:
        if i == ' ':
            out_string += '/ '
        else:
            y = text_to_morse.get(i.upper())
            if y != None:
                out_string += y + ' '
    return out_string

def main(args):
    with open(args.translate_file, 'r') as fp:
        pass
        #TODO add translate function

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('translate_file')
    args = parser.parse_args()
    main(args)
