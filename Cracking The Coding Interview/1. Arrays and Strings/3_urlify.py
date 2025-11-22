# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold additional characters, and that you are given the 'true' length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
def urlify(s, n):
    list1 = []
    final_str = ""
    for i in range(n):
        if s[i] == " ":
            list1.append("%20")
        else:
            list1.append(s[i])
    
    for j in range(len(list1)):
        final_str += list1[j]
    return final_str

# for inplace swaps in the same one
def optimised_urlify(s, n):
    arr = list(s)
    write = len(arr) - 1
    read  = n -1

    while read >=0:
        if arr[read] == " ":
            arr[write] = "0"
            arr[write-1] = "2"
            arr[write-2] = "%"
            write -= 3
        else:
            arr[write] = arr[read]
            write -= 1
        read -=1

    return ''.join(arr)

str1 = "Mr John Smith    "
# print(urlify(str1, 13))
print(optimised_urlify(str1, 13))