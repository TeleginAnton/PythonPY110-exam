import json
import re
import random

import conf

BOOK_JSON = "book.json"
BOOK_TXT = "books.txt"


def _main():
    """Проверка скрипта + запись в json файл"""
    object_python = title(BOOK_JSON)
    with open(BOOK_JSON, "w") as fn:
        json.dump(object_python, fn, indent=4, ensure_ascii=False)


def module():
    ...


def title(test: str) -> dict:
    """Генерация названий книг"""
    with open(BOOK_TXT) as fn:
        res = {i: x for i in fn for x in range(10)}
    return res


if __name__ == '__main__':
    _main()
