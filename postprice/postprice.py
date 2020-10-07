#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests


class PostPrice:
    """
    Класс для расчета стоимости доставки почтовых отправлений Почтой России

    :param from: Почтовый индекс отправителя (6 цифр)
    :param to: Почтовый индекс получателя (6 цифр)
    :param index_from: alias для from
    :param index_to: alias для to
    :param mass: Масса отправления, в граммах (значения от 0 до 20000)
    :param valuation: Объявленная ценность, в рублях
    :param vat: НДС 20% (1 — с НДС, 0 — без НДС)
    :param oversized: Негабаритная посылка (1 — негабаритная, 0 — обычная)
    :param month: Месяц отправки (от 1 до 12)
    :param day: День месяца отправки (от 1 до 31)
    :param date: Устанавливает месяц и день из даты
    :type date: datetime.datetime, datetime.date
    Обязательные параметры запроса: from, to (index_from, index_to).
    """
    url = 'https://postprice.ru/engine/russia/api.php'
    params = {}

    def __init__(self, data=None, **kwargs):
        self._set_fields(data, kwargs)

    def _set_fields(self, data, kwargs):
        """
        >>> from datetime import datetime
        >>> p = PostPrice()
        >>> p._set_fields({'index_from': '630000', 'date': datetime(2019, 1, 2)}, {'index_to': '620000'})
        >>> p.params
        {'from': '630000', 'to': '620000', 'month': 1, 'day': 2}
        >>> p.params = {}
        >>> p._set_fields({'from': '630000', 'to': '620000', 'vat': True}, {'oversized': True})
        >>> p.params
        {'from': '630000', 'to': '620000', 'vat': 1, 'oversized': 1}
        """
        if not data:
            data = {}
        data.update(kwargs)
        for field in ['from', 'index_from', 'to', 'index_to', 'mass', 'valuation', 'vat', 'oversized',
                      'date', 'month', 'day']:
            value = data.get(field)
            if not value:
                continue

            if field in ['vat', 'oversized']:
                value = int(value)
            elif field == 'date':
                self.params['month'] = value.month
                self.params['day'] = value.day
                continue

            field = field[6:] if field in ['index_from', 'index_to'] else field
            self.params[field] = value

    def validate(self):
        for field in ['from', 'to']:
            if not self.params.get(field):
                raise Exception(f'"{field}" field is required.')

    def calculate(self, data=None, **kwargs):
        """
        Запрашивает ресурс postprice.ru для расчета стоимости доставки, возвращает json.
        Обязательные параметры запроса: from, to (index_from, index_to).

        Requests postprice.ru for calculation and returns json result.

        :param from: Почтовый индекс отправителя (6 цифр)
        :param to: Почтовый индекс получателя (6 цифр)
        :param index_from: alias для from
        :param index_to: alias для to
        :param mass: Масса отправления, в граммах (значения от 0 до 20000)
        :param valuation: Объявленная ценность, в рублях
        :param vat: НДС 20% (1 — с НДС, 0 — без НДС)
        :param oversized: Негабаритная посылка (1 — негабаритная, 0 — обычная)
        :param month: Месяц отправки (от 1 до 12)
        :param day: День месяца отправки (от 1 до 31)
        :param date: Устанавливает месяц и день из даты
        :type date: datetime.datetime, datetime.date

        >>> json = PostPrice().calculate(index_from='630000', index_to='620000', mass=40, valuation=500, vat=True)
        >>> json['city_from'] == 'НОВОСИБИРСК' and json['city_to'] == 'ЕКАТЕРИНБУРГ'
        True
        >>> all([field in json for field in ['simple_letter', 'reg_letter', 'val_letter']])
        True
        """
        self._set_fields(data, kwargs)
        self.validate()

        response = requests.get(self.url, params=self.params)
        try:
            return response.json()
        except Exception as exc:
            return None


if __name__ == '__main__':

    def _test_module():
        import doctest
        result = doctest.testmod()
        if not result.failed:
            print(f"{result.attempted} passed and {result.failed} failed.\nTest passed.")

    _test_module()
