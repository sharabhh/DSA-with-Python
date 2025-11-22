# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(str1, str2):
    obj1 = {}
    obj2 = {}

    for i in range(len(str1)):
        if str1[i] in obj1:
            obj1[str1[i]] +=1
        else:
            obj1[str1[i]] = 1

    for j in range(len(str2)):
        if str2[j] in obj2:
            obj2[str2[j]] +=1
        else:
            obj2[str2[j]] = 1
    return obj1 == obj2


s1 = "abcde"
s2 = "abcde"

print(check_permutation(s1, s2))