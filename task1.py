import random

BOOK_TXT = "books.txt"


def _main():
    print(title())


def title():
    with open(BOOK_TXT, encoding='utf8') as fn:
        enum_book = fn.read().splitlines()
        random_str = random.choice(enum_book)
    return random_str


if __name__ == '__main__':
    _main()
