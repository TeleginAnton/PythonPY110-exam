import json
import random

from faker import Faker
from pprint import pprint

from conf import MODEL

BOOK_JSON = "book.json"
BOOK_TXT = "books.txt"


def _main() -> None:
    """
    Формирует список из 100 книг (список словарей) и записывает в файл book.json только один словарь :(
    """
    python_object = generator()
    with open(BOOK_JSON, "w") as function:
        # for word in python_object:
        #     function.write(word + '\n')
        json.dump(python_object, function, indent=4, ensure_ascii=False)


def pk_():
    pk = 1
    while pk <= 100:
        yield pk
        pk += 1
    return pk


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
    num_four_signs = (random.randrange(2000, 2021, 6))
    return num_four_signs


def pages() -> int:
    """
    Функция - генератор.
    :return: Количество страниц - генерируемый объект.
    """
    num_three_signs = (random.randint(100, 200))
    return num_three_signs


def isbn13() -> None:
    """
    Функция - генератор.
    :return: Международный книжный номер - генерируемый объект.
    """
    fake = Faker()
    book_num = (fake.numerify(text='%%%-%-%%%%%-%%%-%') for _ in range(5))
    return next(book_num)


def rating() -> int:
    """
    Функция - генератор.
    :return: Рейтинг - генерируемый объект.
    """
    int_nun = (random.randint(0, 5))
    return int_nun


def price() -> float:
    """
    Функция - генератор.
    :return: Стоимость книги - генерируемый объект.
    """
    float_num = float(random.randint(0, 9000))
    return float_num


def author() -> None:
    """
    Функция - генератор.
    :return: Автор - генерируемый объект.
    """
    fake = Faker()
    one_author = (fake.name())
    return one_author


def fields() -> dict:
    new_fields = {"title": title(), "year": year(),
                  "pages": pages(), "isbn13": isbn13(),
                  "rating": rating(), "price": price(), "author": author()}
    return new_fields


def generator():
    model = MODEL
    for i in pk_():
        res = {"model": model, "pk": i, "fields": fields()}
        pprint(res, sort_dicts=False)
    return res


if __name__ == '__main__':
    _main()
