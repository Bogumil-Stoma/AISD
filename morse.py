import argparse

text_to_morse = dict()

with open('morse.txt', 'r') as fp:
    for line in fp:
        key, value = line.split()
        text_to_morse[key] = value

#text_to_morse.setdefault('')

def convertToMorse(s: str) -> str:
    out_string: str = ''
    s.strip()
    for i in s:
        if i == ' ':
            if out_string[-2:] == '/ ':
                continue
            out_string += '/ '
        else:
            y = text_to_morse.get(i.upper())
            out_string += y + ' ' if y != None else ''
    return out_string.strip()

def main(args):
    with open(args.translate_file, 'r') as fp:
        pass
        #TODO add translate function
        result = ''
        for line in fp:
            result += convertToMorse(line)
            result += '\n'
        print(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('translate_file')
    args = parser.parse_args()
    main(args)
