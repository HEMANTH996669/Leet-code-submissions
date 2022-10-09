str = input("take input")
def find(str):
    l = list(str)
    n = len(l)
    count = 0
    for i in range(0,n):
        if(l[i] == l[0]):
            count = count + 1
    if(count == len(l)):
        return "impossible"
        exit()
    low = 0
    high = len(l)-1
    while low < high:
        if(l[low]>l[low+1]):
            l[low]=l[low+1]
            break
        low = low+1
    st = ''.join(l)
    return(st)
print(find(str))


