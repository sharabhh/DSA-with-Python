# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def unique_string(strr):
    if len(strr) == 1:
        return True
    
    for i in range(len(strr) - 1):
        for j in range(i+1, len(strr)):
            if strr[i] == strr[j]:
                return False
    
    return True


str1 = "sshar"
print(unique_string(str1))