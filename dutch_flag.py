# Dutch flag problem. basically sort an array of possible values of 0,1,2.
```
EXAMPLE I/P:
    2
    5
    0 2 1 2 0
    3
    0 1 0

EXAMPLE O/P:
    0 0 1 2 2
    0 0 1



# Below implementation has a time complexity of O(n).
# can be done by sorting with maintaing 3 pos in the array, but this is simpler.

def simple():    
    for _ in range(int(input())):
        arrN = int(input())
        arr = input()
        arrL = list(map(int, arr.split()))
        
        zeroesAndOnes = []
        twos = []
        for digit in arrL:
            if digit == 0:
                zeroesAndOnes.insert(0, digit)
            elif digit == 1:
                zeroesAndOnes.append(digit)
            else:
                twos.append(digit)
        zeroesAndOnes.extend(twos)
        print(zeroesAndOnes)
        
# Below implementation has a time complexity of O(n) with constant space complexity.
def withSorting():
    for _ in range(int(input())):
        arrN = int(input())
        arr = input()
        arrL = list(map(int, arr.split()))
        
        low = 0
        mid = 0
        high = arrN - 1
        
        while(mid <= high):
            if arrL[mid] == 0:
                arrL[low], arrL[mid] = arrL[mid], arrL[low]
                low = low+1
                mid = mid+1
            elif arrL[mid] == 1:
                mid = mid+1
            elif arrL[mid] == 2:
                arrL[high], arrL[mid] = arrL[mid], arrL[high]
                high = high -1
        print(arrL)
        
        
#simple()
#withSorting()
        
    
