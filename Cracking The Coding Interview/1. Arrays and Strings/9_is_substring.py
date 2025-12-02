#Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubstrin g [e.g., "waterbottle " is a rotation oP'erbottlewat") 


def is_substring(s1, s2):
    if(len(s1) == 0 or len(s1)!= len(s2)):
        return False
    
    x = s1 + s1
    if s2 in x:
        return True
    return False
    
str1= "abcd"
str2= "dacb"
print(is_substring(str1, str2))