# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edit) away.

def one_away(s1, s2):
    if abs(len(s1) - len(s2)):
        return False
    if len(s1)< len(s2):
        short_string, long_string = s1, s2
    else:
        short_string, long_string = s2, s1
    i=0
    j=0
    found_diff = False

    while i < len(short_string) and j < len(long_string):
        if short_string[i] != long_string[j]:
            if found_diff:
                return False #since this was the second difference
            if len(short_string) == len(long_string):
                i+=1
                j+=1
            else:
                j+=1
        else:
            i+=1
            j+=1


    return True

string1 = "pale"
string2 = "pales"
print(one_away(string1, string2))