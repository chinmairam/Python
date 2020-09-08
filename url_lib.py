# urllib

import urllib.request as url
# dir(urllib)

page = url.urlopen('http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')
# print(page)
text = page.read() # Prints in bytes format of text
text = text.decode() # Text
page.close()

file = open('raven.txt','w')
# print(file)
file.write(text)
file.close()

file = file.split()
book = {}

##for word in file:
##    if word not in book:
##        book[word] = 1
##    else:
##        book[word] += 1
##
##def last(x):
##    return x[-1]
##
##book = book.items()
##sort_book = sorted(book,key=last,reverse=True)
##for i in sort_book[:10]:
##    print(i[0], ':', i[1])
##    
##
##print(len(book))
##print(len(file))
