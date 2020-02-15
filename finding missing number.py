def FindMissingNum(L):
    n = len(L)
    total = (n+1)*(n+2)/2
    sum_of_list = sum(L)
    return total-sum_of_list
L1 = [1,2,3,4,5]
L2 = [2,3,1,0,5]
FindMissingNum(L1)
