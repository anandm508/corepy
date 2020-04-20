"""Retreive and print words from a URL.

Usage:

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of word from a URL.

    Args:
        url : The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words 

    from the document"""
    story_words = []
    story = urlopen(url)
    # story = urlopen('https://sixty-north.com/c/t.txt')

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    """Prints item one per line
    Args:
        An iterable series of printable items.

    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from ata URL.

        Args:
        url : The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
