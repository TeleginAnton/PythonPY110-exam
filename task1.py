def _main():
    print(title())


def decorator(fn):
    max_len_book = 87

    def wrapper(*args):
        result = fn(args)
        if result > max_len_book:
            raise ValueError(f"длина книги больше заданого условия max_len_book: {max_len_book}")

        return result

    return wrapper


@decorator
def title(fn):
    with open("books.txt", encoding="utf8") as fn:
        len_book = fn.readlines()
        max_str_book = max(len(i) for i in len_book)
        print(f"проверка длины книги = {max_str_book}")
    return max_str_book


if __name__ == '__main__':
    _main()
