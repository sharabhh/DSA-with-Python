# Given a string, write a function to check if it is a permutation of a palindrome.

def palindrome_permutation(s):
    arr = list(s.lower())
    obj = {}
    for i in range(len(arr)):
        if arr[i] == " ":
            continue
        if arr[i] in obj:
            obj[arr[i]] += 1
        else:
            obj[arr[i]] = 1
    
    odd_count = 0
    for count in obj.values():
        if count%2 != 0:
            odd_count +=1

    return odd_count<=1


str1 = "Tact Coa"
print(palindrome_permutation(str1))
