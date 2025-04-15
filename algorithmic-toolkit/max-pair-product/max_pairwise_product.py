import random
import timeit
import time
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
def max_pairwise_product_fast_sort(numbers):
    numbers=numbers[:]
    numbers.sort()
    return numbers[-1]*numbers[-2]
def max_pairwise_product_fast(numbers):
    if (len(numbers)<2): return 0
    max1_i=0
    for i in range(len(numbers)):
        max1_i= i if numbers[i]>numbers[max1_i] else max1_i
    max2_i= 0 if max1_i!=0 else 1
    for i in range(len(numbers)):
        max2_i= i if i!=max1_i and numbers[i]>numbers[max2_i] else max2_i
    return numbers[max1_i]*numbers[max2_i]
def max_pairwise_product_parallel(numbers):
    if len(numbers)<2 : return 0
    max1_i=0
    max2_i=1
    for i in range(len(numbers)):
        if numbers[max1_i]<numbers[i]: 
            max2_i, max1_i=max1_i, i
        elif i!=max1_i and numbers[max2_i]<numbers[i]:
            max2_i= i
    return numbers[max1_i]*numbers[max2_i]
if __name__ == '__main__':
    # -----------------------------------
    # STRESS TEST WITH RUNTIME COMPARISON
    # -----------------------------------
    # while(True):
    #     randnums=[]
    #     n= random.randint(2,10**4)
    #     print(f'list len: {n}')
    #     for i in range(n):
    #         randnums.append(random.randint(1,10**6))
    #     stime= time.time()
    #     max1=max_pairwise_product_fast_sort(randnums)
    #     time1=time.time()-stime
    #     stime= time.time()
    #     max2=max_pairwise_product_fast(randnums)
    #     time2=time.time()-stime        
    #     if(max1!=max2):
    #         print(f'function 1: {max1}, function 2: {max2}')
    #         break
    #     print(f'OK- {'function 1' if time1<time2 else 'function 2'} is faster')
    # ---------------------------------------------------------------------------
    # RUNTIME COMPARISON WITH TIMEIT
    # ---------------------------------------------------------------------------
    # input= [random.randint(1,10**5) for _ in range(10**6)]
    # print(timeit.timeit(lambda: max_pairwise_product_fast(input),number=1)<timeit.timeit(lambda: max_pairwise_product_fast_sort(input),number=1))
    # ---------------------------------------------------------------------------
    # MAIN
    # ---------------------------------------------------------------------------
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_parallel(input_numbers))
    
    
    
    

