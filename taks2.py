
BOOK_TXT = "books.txt"


def _main():
    title()


def decorator(fn):
    max_len_book = 85

    def wrapper(*args):
        result = fn(args)
        if result > max_len_book:
            raise ValueError(f"длина книги больше заданого условия max_len_book: {max_len_book}")

        return result

    return wrapper


@decorator
def title(fn):
    with open(BOOK_TXT, encoding='utf8') as fn:
        enum_book = fn.read().splitlines()
        max_str_book = max(len(i) for i in enum_book)
        print(f"проверка максимальной длины книги = {max_str_book}")
    return max_str_book


if __name__ == '__main__':
    _main()
