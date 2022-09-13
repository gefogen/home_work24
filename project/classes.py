import re
from typing import Iterator, List, Iterable, Union

from project.exceptions import NotTypeError, NotValueError


class Search:

    def filter(self: Iterator, string_to_search: str) -> Iterable:
        """Получить данные, которые содержат указанный текст"""
        if not isinstance(string_to_search, str):
            raise NotTypeError
        return list(filter(lambda line: string_to_search in line, self))

    def sort(self: Iterator, order: str = 'asc') -> List:
        """Сортировка данных в порядке возрастания или убывания"""
        if order not in ('asc', 'desc'):
            raise NotValueError
        if order == 'desc':
            return sorted(self, reverse=True)
        return list(sorted(self, reverse=False))

    def map(self: Iterator, column: Union[str, int]) -> Iterable:
        """Получить указанный столбец"""
        regex = re.compile(r'(?: - - \[)|(?:\] ")|(?:" ")|(?: \")|(?:\" )')
        if not str(column).isdigit():
            raise NotTypeError
        return map(lambda line: regex.split(line)[int(column)], self)

    def limit(self: Iterator, number: Union[str, int]) -> List:
        """Количество строк, возвращаемые переданным числом"""
        if not str(number).isdigit():
            raise NotTypeError
        return list(self)[:int(number)]

    def unique(self: Iterator) -> Iterable:
        """Возвращать уникальные строки"""
        return set(self)

    def regex(self: Iterator, text: str) -> Iterable:
        """Фильтрация по регулярному выражению"""
        regex = re.compile(rf'{str(text)}')
        return filter(lambda line: regex.search(line), self)
