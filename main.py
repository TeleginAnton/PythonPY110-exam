import random
import json

from faker import Faker
from pprint import pprint
from typing import List, Any

from conf import MODEL

BOOK_JSON = "book.json"
BOOK_TXT = "books.txt"

fake = Faker()


def _main() -> Any:
    """
    Формирует список из 100 книг (список словарей) и записывает в файл book.json.
    """
    # pprint([next(generator_book()) for _ in range(5)], sort_dicts=False)
    json_list = []
    count = 1
    for i in generator_book():
        if count > 15:
            break
        json_list += [i]
        count += 1
        # pprint(json_list, sort_dicts=False)

    with open(BOOK_JSON, "w", encoding='utf8') as function:
        json.dump(json_list, function, indent=4, ensure_ascii=False)


def generator_book(counter: int = 0):
    while True:
        counter += 1
        yield {"model": MODEL, "pk": counter, "fields": fields()}


def title() -> str:
    """
    Функция - генератор.
    :return: Названием книги - генерируемый объект.
    """
    with open(BOOK_TXT, encoding='utf8') as fn:
        enum_book = fn.read().splitlines()
        random_str = random.choice(enum_book)
    return random_str


def year() -> int:
    """
    Функция - генератор.
    :return: Год издания - генерируемый объект.
    """
    return random.randrange(2000, 2021, 6)


def pages() -> int:
    """
    Функция - генератор.
    :return: Количество страниц - генерируемый объект.
    """
    return random.randint(100, 200)


def isbn13() -> None:
    """
    Функция - генератор.
    :return: Международный книжный номер - генерируемый объект.
    """
    for _ in range(5):
        fake.isbn13()
    return fake.isbn13()


def rating() -> float:
    """
    Функция - генератор.
    :return: Рейтинг - генерируемый объект.
    """
    return round(random.uniform(0, 10), 1)


def price() -> float:
    """
    Функция - генератор.
    :return: Стоимость книги - генерируемый объект.
    """
    return round(random.uniform(0, 1500), 2)


def author():
    """
    Функция - генератор.
    :return: Автор - генерируемый объект.
    """
    test = []
    for _ in range(random.randint(1, 3)):
        for i in [fake.name()]:
            test += [i]
    return test


def fields() -> dict:
    new_fields = {"title": title(), "year": year(),
                  "pages": pages(), "isbn13": isbn13(),
                  "rating": rating(), "price": price(), "author": author()}
    return new_fields


if __name__ == '__main__':
    _main()
