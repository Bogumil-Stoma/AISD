from pattern_sarch import searchN, searchKMP, searchKR
import gc, time
import matplotlib.pyplot as plt

NUM_OF_MEASUREMENTS = 1
INTERVAL = 100
MAX_NUM_OF_WORDS = 1000

def measure_time(func , n: int, wordlist: list[str], text: str):
    current_wordlist = wordlist[:n]
    for _ in range(NUM_OF_MEASUREMENTS):
        sum = 0
        for word in current_wordlist:
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            func(word, text)
            stop = time.process_time()
            if gc_old: gc.enable()
            sum += stop-start

    return sum/NUM_OF_MEASUREMENTS


def main():
    # text = 'Ala ma małego kota małego kota ala ala małegolmaolmao lol'
    # pattern = 'małego'
    # print(searchKR(pattern, text))
    text = ""
    word_list = []
    with open('pan-tadeusz.txt', 'r', encoding='utf-8') as fp:
        fp.seek(0)
        for line in fp:
            word_list.extend(map(str.lower, line.split()))
            text+=line.lower()

    x_list = []
    naive_list = []
    for i in range(INTERVAL, MAX_NUM_OF_WORDS+1, INTERVAL):
        print("Measuring NAIVE. Progress: {0}/{1}".format(round(i/INTERVAL), round(MAX_NUM_OF_WORDS/INTERVAL)), end='\r')
        x_list.append(i)
        naive_list.append(measure_time(searchN, i, word_list, text))
    
    kmp_list = []
    for i in x_list:
        print("Measuring KMP. Progress: {0}/{1}".format(round(i/INTERVAL), round(MAX_NUM_OF_WORDS/INTERVAL)), end='\r')
        kmp_list.append(measure_time(searchKMP, i, word_list, text))
    
    # kr_list = []
    # for i in x_list:
    #     print("Measuring KMP. Progress: {0}/{1}".format(round(i/INTERVAL), round(MAX_NUM_OF_WORDS/INTERVAL)), end='\r')
    #     kr_list.append(measure_time(searchKR, i, word_list, text))
    
    
    print(end='\033[K')
    print("\r Measurements complete")

    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.suptitle('Pattern search algorithms')
   

    plt.plot(x_list, naive_list, label="Naive")
    plt.plot(x_list, kmp_list, label="KMP")
    # plt.plot(x_list, kr_list, label="KR")
    
    plt.legend()
    plt.savefig('pattern_search.png')
    plt.show()

if __name__ == "__main__":
    main()