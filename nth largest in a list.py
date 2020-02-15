"""finding second or nth largest number in a list"""
import heapq as h
def n_largest():
    l = [int(i) for i in input().split() ]
    h.heapify(l)
    k = h.nlargest(2,l)
    return k[1]