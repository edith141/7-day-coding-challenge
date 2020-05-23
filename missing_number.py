'''
Coding Challenge #3
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4.
'''

for _ in range(int(input())):
    N = int(input())
    arr = input()
    arrL = list(map(int, arr.split()))

#   FIRST WAY [ O(1) time complexity ]
#------------------
#   Most efficient approach. Since I know only one item would be missing from the array of N seq numbers, 
#   I can just subtract the sum of array from the sum of N numbers.
    
    print( int(N*(N+1)/2 - sum(arrL)) )
  
  

#   SECOND WAY [ O(N) time complexity ]
#------------------
#   I can store the values seen while scanning the arr to a hashtable and iterate over it to find which value is not present. 
#   Can be done for multiple values being absent, so more generalized appraoch.
    
    arrHash = {}
    
    # setting key of the value(s) in the array to True 
    for num in arrL:
        arrHash[num] = True
        
    # Iterating and checking key for each number from 1 to N.
    # As we see a missing key for any number, we stop since we got the missing number.
    # Can go on if we need to check for more than one missing values though.
    for i in range(1, N+1):
        # print(i)
        if arrHash.get(i) != True:
            print(i)
            break
        
        
        
#   THIRD WAY [ O(N) time complexity ]
#------------------
#   Sort the input array and check for missing number.
#   Base case can be checking if the array starts with 1 and ends with N.
#   If yes, check for other possible values as well.

    # sorting the arr
    sortedArr = sorted(arrL)
    
    # checking for base cases of 1 and N being present or not
    # proceed only if both are present, else print the num and break.
    if sortedArr[0] != 1:
        print(1)
        break
    elif sortedArr[N-2] != N:
        print(N)
        break
    # base cases true, then proceed to check if 
    #   1) the current arr number is one more than the last number
    #   2) the current arr number is one less than the next number
    # print and exit if any condition is true.
    else:
        for i in range(1, N-1):
            if sortedArr[i] != sortedArr[i-1]+1:
                print(sortedArr[i-1]+1)
                break
            elif sortedArr[i] != sortedArr[i+1]-1:
                print(sortedArr[i+1]-1)
                break
                
    
