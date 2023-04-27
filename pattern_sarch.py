

def searchN(word: str, text: str) -> int:
    w_len = len(word)
    t_len = len(text)

    for i in range(t_len - w_len + 1):
        if text[i:i+w_len] == word:
            return i
    return -1


def searchKMP():
    pass

def searchKR():
    pass