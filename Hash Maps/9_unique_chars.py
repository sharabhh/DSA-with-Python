def has_unique_chars(str):
    new_set = list(set(str))
    if sorted(str) == sorted(new_set):
        return True
    return False

print(has_unique_chars("hello")) 