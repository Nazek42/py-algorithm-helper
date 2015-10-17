def quicksort(L):
    if len(L) > 1:
        pivot_index = len(L) // 2
        smaller = []
        larger = []
        for i, val in enumerate(L):
            if i != pivot_index:
                if val < L[pivot_index]:
                    smaller.append(val)
                else:
                    larger.append(val)
        quicksort(smaller)
        quicksort(larger)
        L[:] = smaller + [L[pivot_index]] + larger        
