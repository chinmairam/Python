def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    print(last_letter)
    return sorted(strings, key=last_letter)

print(sort_by_last_letter(['hello', 'from', 'a', 'local', 'function']))
