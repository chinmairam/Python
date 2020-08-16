def initials(phrase):
    result = ""
    for word in phrase.split():
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) 
print(initials("local area network")) 