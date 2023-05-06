

def searchN(word: str, text: str):
    w_len = len(word)
    t_len = len(text)
    res = []
    if w_len == 0 or t_len == 0 or w_len > t_len:
        return res

    for i in range(t_len - w_len + 1):
        if text[i:i+w_len] == word:
            res.append(i)
    return res




def KMPNext(pattern):
    KMPTable = [0]*len(pattern)
    KMPTable[0] = 0
    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j+=1
            KMPTable[i] = j
            i+=1

        else:
            if j != 0:
                j = KMPTable[j-1]
            else:
                KMPTable[i] = 0
                i+=1
    return KMPTable


def searchKMP(pattern, text):
    pat_len = len(pattern)
    text_len = len(text)
    res = []
    if pat_len==0 or text_len==0 or pat_len>text_len:
        return res

    table = KMPNext(pattern)
    i, j = 0, 0
    while (text_len - i) >= (pat_len - j):
        if pattern[j] == text[i]:
            i+=1
            j+=1
        if j == pat_len:
            res.append(i-j)
            j = table[j-1]
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = table[j-1]
            else:
                i += 1

    return res




def searchKR(pattern, text, diff_letters = 256, prime_number = 101):
    pat_len = len(pattern)
    text_len = len(text)
    res = []

    if pat_len==0 or text_len==0 or pat_len>text_len:
        return res
    
    pat_hash = 0
    text_hash = 0
    h = 1
    

    for i in range(pat_len-1):
        h = (h*diff_letters) % prime_number

    for i in range(pat_len):
        pat_hash = ord(pattern[i])*(2**(pat_len-i-1))+pat_hash
        text_hash = ord(text[i])*(2**(pat_len-i-1))+text_hash

        '''pat_hash = (diff_letters * pat_hash + ord(pattern[i])) % prime_number
        text_hash = (diff_letters * text_hash + ord(text[i])) % prime_number'''

    for i in range(text_len-pat_len+1):
        if pat_hash == text_hash:
            for j in range(pat_len):
                if text[i+j] != pattern[j]:
                    break
                if (j+1) == pat_len:
                    res.append(i)

        if i < (text_len - pat_len):
            text_hash = (text_hash-ord(text[i])*(2**(pat_len-1)))*2 + ord(text[i+pat_len])
            '''text_hash = (diff_letters*(text_hash-ord(text[i])*h) + ord(text[i+pat_len])) % prime_number
            if text_hash < 0:
                text_hash += prime_number'''

    return res
