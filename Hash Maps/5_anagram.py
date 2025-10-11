def group_anagram(strings):
    anagram_string = {}
    for string in strings:
        sortedWord = "".join(sorted(string))
        if sortedWord in anagram_string:
            anagram_string[sortedWord].append(string)
        else:
            anagram_string[sortedWord] = [string]
    return list(anagram_string.values())

print(group_anagram(['eat', 'tea', 'tan', 'ant', 'bat']))