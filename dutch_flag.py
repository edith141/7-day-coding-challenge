# Dutch flag problem. basically sort an array of possible values of 0,1,2.
# Below implementation has a time complexity of O(n) with constant space complexity.
# can be done by sorting with maintaing 3 pos in the array, but this is simpler.

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
