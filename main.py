from matplotlib import pyplot as plt
import sort
import time
import gc

text = []

with open('pan-tadeusz.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        text.extend(map(str.lower, line.split()))


def measure_time(func, n, text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    func(text[:n])
    stop = time.process_time()
    if gc_old: gc.enable()
    return stop-start
