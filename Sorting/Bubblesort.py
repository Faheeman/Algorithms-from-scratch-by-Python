def swap(lis, num1, num2):
    temp = lis[num1]
    lis[num1] = lis[num2]
    lis[num2] = temp
    return lis


def Bubble(lis):
    n = len(lis)
    for i in range(n - 1): 
        for j in range(n - 1 - i):  
            if lis[j] > lis[j + 1]:
                swap(lis, j, j + 1)
    return lis

if __name__=='__main__':
    lis=[3,2,1,3,2]
    liste=Bubble(lis)
    print(liste)       
    