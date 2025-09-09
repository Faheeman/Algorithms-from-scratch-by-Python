def swap(lis,num1,num2):
    temp=lis[num1]
    lis[num1]=lis[num2]
    lis[num2]=temp
    return lis
def selection(lis):
    n=len(lis)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lis[j] < lis[min_index]:
                min_index = j
        swap(lis, i, min_index)
    return lis
            
if __name__=="__main__":
    lis=[5,3,4,2,6,1]
    listed=selection(lis)
    print(listed)
