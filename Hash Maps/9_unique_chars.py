def has_unique_chars(str):
    new_set = set()
    for s in str:
        if s in new_set:
            return False
        new_set.add(s)
    return True

print(has_unique_chars("helo")) 