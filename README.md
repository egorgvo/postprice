# postprice
Библиотека Python для расчета стоимости почтовых отправлений Почтой России.

Бибиотека использует API ресурса [postprice.ru](https://postprice.ru/api/).

#### Версия Python

Версия, на которой велась разработка - 3.8, но функционал должен работать для любой версии Python 3.

### Installation

```bash
pip install postprice
```

### Usage examples

```python
from postprice import PostPrice
json = PostPrice().calculate(index_from='630000', index_to='620000', mass=40, valuation=500, vat=True)
```

Другой вариант вызова:

```python
post = PostPrice(index_from='630000', valuation=500, vat=True)
json = post.calculate(index_to='620000', mass=40)
```

Пример json-ответа:
```python
{
    'code': 100, 
    'locality_from': 'НОВОСИБИРСК ПОЧТАМТ', 
    'locality_to': 'ЕКАТЕРИНБУРГ', 
    'city_from': 'НОВОСИБИРСК', 
    'city_to': 'ЕКАТЕРИНБУРГ', 
    'region_from': 'НОВОСИБИРСКАЯ ОБЛАСТЬ', 
    'region_to': 'СВЕРДЛОВСКАЯ ОБЛАСТЬ', 
    'simple_letter': 31.2, 
    'reg_letter': 68.4, 
    'val_letter': 159.2, 
    'simple_parcel': 48, 
    'reg_parcel': 84, 
    'val_parcel': 164, 
    'pkg': 284.34, 
    'ems': 727.52, 
    'letter_reg_1class': 144, 
    'letter_val_1class': 228, 
    'reg_parcel1class': 186, 
    'val_parcel1class': 252, 
    'pkg_1class': 179, 
    'pkg_val_1class': 283, 
    'cod': 605
}
```

#### Описание параметров

**from** - Почтовый индекс отправителя (6 цифр).  
**to** - Почтовый индекс получателя (6 цифр).
**index_from** - alias для from.  
**index_to** - alias для to.  
**mass** - Масса отправления, в граммах (значения от 0 до 20000).  
**valuation** - Объявленная ценность, в рублях.  
**vat** - НДС 20% (1 — с НДС, 0 — без НДС). Возможна подача boolean.  
**oversized** - Негабаритная посылка (1 — негабаритная, 0 — обычная). Возможна подача boolean.  
**month** - Месяц отправки (от 1 до 12).  
**day** - День месяца отправки (от 1 до 31).  
**date** - Дата типа datetime.datetime (или datetime.date), подается вместо month и date.    

Обязательные параметры запроса: from, to. 


### Changelog

#### 1.0.0 (2020-10-07)

- Первая рабочая версия

#### Теги
Почта России, доставка, почта, письмо, посылка, pochta.ru, russian post, russianpost