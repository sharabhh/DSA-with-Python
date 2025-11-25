# Implement a method to perform basic string compression using the counts of repeated characters. 
# two pointer then calculate the diff between them

def string_compression(s1):
    i= 0
    j=1
    count = 1
    s2 = ""

    while j < len(s1):
        if s1[i] == s1[j]:
            count+=1
            j+=1
        else:
            s2+=s1[i] + str(count)
            i=j
            j+=1
            count = 1

    s2 += s1[i] + str(count) 
    return s2

string1 = "aabbcccdddddee"
print(string_compression(string1))