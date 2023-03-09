import argparse

text_to_morse = dict()

with open('morse.txt', 'r') as fp:
    for line in fp:
        key, value = line.split()
        text_to_morse[key] = value

def main(args):
    with open(args.translate_file, 'r') as fp:
        pass
        #TODO add translate function

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('translate_file')
    args = parser.parse_args()
    main(args)