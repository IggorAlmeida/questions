def slidingWindow(array,k):

    tamanho = len(array)
    if k <=0 and k>tamanho:
        return 0

    max_sum = sum(array[:k])
    sum_atual = max_sum
    
    for i in range(0,len(array)-k):
        sum_atual = sum_atual - array[i] + array[k+i]
        max_sum = max(max_sum,sum_atual)

    return max_sum

if __name__=="__main__":
    list_num = [1,-40,23,10,23,50,-33,28]
    window = 3
    print(slidingWindow(list_num,window))