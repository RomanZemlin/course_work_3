import utils
import re
from _datetime import datetime


def main():
    """
    Функция получает отсортированные 5 последних операций клиента
    :return: Возвращает сообщение о 5 последних операциях в формате :
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>
    в списке
    """
    data = utils.output()
    operations = []
    for i in data:
        date = i.get('date')
        description = i.get('description')
        of = i.get('from')
        amount = i.get('operationAmount')['amount']
        currency = i.get('operationAmount')['currency']['name']
        if of is not None:
            """Если данные откуда был перевод не пустой, то продолжает работу по коду ниже"""
            # Воспользовался datetime для приведения даты в фотрмат дд-мм-гггг
            normal_date = datetime.strptime(date[:10], '%Y-%m-%d')
            formatted_date = normal_date.strftime('%d-%m-%Y')
            number_one = filter(str.isdecimal, i.get('from'))
            number_two = filter(str.isdecimal, i.get('to'))
            # Создал две переменные которые фильтруются, возвращает истину если все символы десятичные
            word_one = re.sub(r'[^\w\s]+|\d+', r'', i.get('from')).strip()
            word_two = re.sub(r'[^\w\s]+|\d+', r'', i.get('to')).strip()
            # Создал две переменные которые убирают все буквы оставляя только номера карт и счетов
            composed_number_one = "".join(number_one)
            composed_number_two = "".join(number_two)
            # Создал две переменные которые соединяют получившиеся номера карт и счетов
            step = 4
            chunks_one = [composed_number_one[i:i + step] for i in range(0, len(composed_number_one), step)]
            chunks_two = [composed_number_two[i:i + step] for i in range(0, len(composed_number_two), step)]
            assembled_piece_one = ' '.join(chunks_one)
            assembled_piece_two = ' '.join(chunks_two)
            card = assembled_piece_one[:7] + '** ****' + assembled_piece_one[15:]
            bank_account = word_two + ' **' + assembled_piece_two[20:]
            # Собираю из кусков название карты или счет совместно с их номерами заменив некоторые значения на *
            operations.append(f"""{formatted_date} {description}
{word_one} {card} -> {bank_account}
{amount} {currency}\n""")

        else:
            """Если данные откуда был перевод пустой, то продолжает работу по коду ниже"""
            # Воспользовался datetime для приведения даты в фотрмат дд-мм-гггг
            normal_date = datetime.strptime(date[:10], '%Y-%m-%d')
            formatted_date = normal_date.strftime('%d-%m-%Y')
            number_two = filter(str.isdecimal, i.get('to'))
            word = re.sub(r'[^\w\s]+|\d+', r'', i.get('to')).strip()
            composed_number = "".join(number_two)
            step = 4
            chunks = [composed_number[i:i + step] for i in range(0, len(composed_number), step)]
            assembled_piece_two = ' '.join(chunks)
            bank_account = word + ' **' + assembled_piece_two[20:]
            # Тут абсолютно тоже самое что и выше но для перевода где from пустой
            operations.append(f"""{formatted_date} {description}
{bank_account}
{amount} {currency}\n""")
    return operations


for i in main():
    print(i)
