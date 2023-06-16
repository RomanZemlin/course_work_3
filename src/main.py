from src import utils
import re


def main():
    data = utils.output()
    for i in data:
        date = i.get('date')
        description = i.get('description')
        of = i.get('from')
        to = i.get('to')
        amount = i.get('operationAmount')['amount']
        currency = i.get('operationAmount')['currency']['name']
        if of is not None:
            number_one = filter(str.isdecimal, i.get('from'))
            number_two = filter(str.isdecimal, i.get('to'))
            word_one = re.sub(r'[^\w\s]+|[\d]+', r'',i.get('from')).strip()
            word_two = re.sub(r'[^\w\s]+|[\d]+', r'',i.get('to')).strip()
            composed_number_one = "".join(number_one)
            composed_number_two = "".join(number_two)
            step = 4
            chunks_one = [composed_number_one[i:i + step] for i in range(0, len(composed_number_one), step)]
            chunks_two = [composed_number_two[i:i + step] for i in range(0, len(composed_number_two), step)]
            assembled_piece_one = ' '.join(chunks_one)
            assembled_piece_two = ' '.join(chunks_two)
            card = assembled_piece_one[:7] + '** ****' + assembled_piece_one[15:]
            bank_account = word_two + ' **' + assembled_piece_two[20:]
            print(f"""{date[:10]} {description}
{word_one} {card} -> {bank_account}
{amount} {currency}\n""")

        else:
            number_two = filter(str.isdecimal, i.get('to'))
            word = re.sub(r'[^\w\s]+|[\d]+', r'', i.get('to')).strip()
            composed_number = "".join(number_two)
            step = 4
            chunks = [composed_number[i:i + step] for i in range(0, len(composed_number), step)]
            assembled_piece_two = ' '.join(chunks)
            bank_account = word + ' **' + assembled_piece_two[20:]
            print(f"""{date[:10]} {description}
{bank_account}
{amount} {currency}\n""")


main()
