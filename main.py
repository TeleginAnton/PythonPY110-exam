import json
import re
import random
import faker

from faker import Faker
from collections import OrderedDict

from conf import MODEL

BOOK_JSON = "book.json"
BOOK_TXT = "books.txt"


def _main():
    """
    Заполнить после оформления!
    :return:
    """
    # print(book_dict())
    # print(next(year()))
    # print(next(pages()))
    # print(next(isbn13()))
    # print(next(rating()))
    # print(next(price()))
    # print(next(author()))
    # with open(BOOK_JSON, "w") as function:
    #     json.dump(python_object, function, indent=5, ensure_ascii=False)


def book_dict():  # todo застрял тут( Можно подсказку?
    """
    Заполнить после оформления!
    :return:
    """
    def decorator(f):
        ...

        def wrapper(*args):
            ...

            return

        return wrapper

    return decorator


# todo Андрей Александрович, как избавиться от переноса строки? Нужен генератор или генератор словарей?
@book_dict()
def title() -> dict:
    """
    Функция - генератор.
    :return: Названием книги - генерируемый объект.
    """
    with open(BOOK_TXT, encoding='utf8') as fn:
        key = ["model"]
        str_py = fn.readlines()
        random_str = random.choices(str_py)
        res = {i: x for i, x in zip(key, random_str)}
    yield res


@book_dict()
def year() -> int:
    """
    Функция - генератор.
    :return: Год издания - генерируемый объект.
    """
    num_four_signs = (random.randrange(2000, 2021, 6))
    yield num_four_signs


@book_dict()
def pages() -> int:
    """
    Функция - генератор.
    :return: Количество страниц - генерируемый объект.
    """
    num_three_signs = (random.randint(100, 200))
    yield num_three_signs


# todo не смог вызвать метод fake.isbn10(). В документации нашёл такой выход.
#  Почему в yield приходится прописывать next?
@book_dict()
def isbn13() -> int:
    """
    Функция - генератор.
    :return: Международный книжный номер - генерируемый объект.
    """
    fake = Faker()
    book_num = (fake.numerify(text='%%%-%-%%%%%-%%%-%') for _ in range(5))
    yield next(book_num)


@book_dict()
def rating() -> int:
    """
    Функция - генератор.
    :return: Рейтинг - генерируемый объект.
    """
    int_nun = (random.randint(0, 5))
    yield int_nun


@book_dict()
def price() -> float:
    """
    Функция - генератор.
    :return: Стоимость книги - генерируемый объект.
    """
    float_num = float(random.randint(0, 9000))
    yield float_num


@book_dict()
def author() -> str:
    """
    Функция - генератор.
    :return: Автор - генерируемый объект.
    """
    author_count = 1
    fake = Faker()
    author_gen = (fake.name() for _ in range(author_count))
    yield next(author_gen)


if __name__ == '__main__':
    _main()
