import os
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    cont = 0
    pair = set()
    for num in ar:
        if num in pair:
            pair.remove(num)
            cont+=1
        else:
            pair.add(num)
    
    return cont 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
