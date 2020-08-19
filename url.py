"""Retrieve and print words from a URL."""

from urllib.request import urlopen

def fetch_words():
    """Fetch a list of words from a URL."""
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        #line_words = line.split()
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main():
    # print(fetch_words())
    words = fetch_words()
    print_items(words)
# print(fetch_words())
# print(__name__)

if __name__ == '__main__':
    main()

# HTTP data is provided as bytes.So 'b' is prefixed.
# Use bytes.decode() to get strings
