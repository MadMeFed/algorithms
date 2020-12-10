import random

def BubleSort(a) :
    for i in range(0,len(a) - 1) :
        for j in range(i + 1 ,len(a)) :
            if (a[i] < a[j]) : 
               a[i] , a[j] = a[j] , a[i]
           
                
def SelectionSort(a) :
    for i in range(0,len(a) - 1):
        min_i = i
        for j in range(i + 1, len(a)) :
            if (a[j] > a[min_i]) :
                min_i = j
        a[i] , a[min_i] = a[min_i] , a[i]

def InsectionSort(a) :
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key > a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key 

def main() :
    randomList = []
    n = 100
    for i in range(0,n):
        randomList.append(random.randint(0,n))

    ar1 = randomList.copy()
    ar2 = randomList.copy()
    ar3 = randomList    

    BubleSort(ar1)
    SelectionSort(ar2)
    InsectionSort(ar3)
    print(ar1[0],ar1[-1])
    print(ar2[0],ar2[-1])
    print(ar3[0],ar3[-1])

if __name__ == "__main__" :
    main()
