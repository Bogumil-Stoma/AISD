

def searchN(word: str, text: str) -> int | None:
    w_len = len(word)
    t_len = len(text)
    res = []
    if w_len == 0 or t_len == 0 or w_len > t_len:
        return res
    
    for i in range(t_len - w_len + 1):
        if text[i:i+w_len] == word:
            res.append(i)
    return res


def searchKMP():
    pass

def searchKR():
    pass