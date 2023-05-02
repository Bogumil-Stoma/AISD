from pattern_sarch import KMP, KMPNext, KR

def main():
    text = 'Ala ma małego kota małego kota ala ala małegolmaolmao lol'
    pattern = 'małego'
    print(KMP(pattern, text))

if __name__ == "__main__":
    main()