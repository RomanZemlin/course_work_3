from utils import output


def main():
    data = output()
    for i in data:
        date = i.get('date')
        description = i.get('description')
        of = i.get('from')
        to = i.get('to')
        amount = i.get('operationAmount')['amount']
        currency = i.get('operationAmount')['currency']['name']
        if of is not None:
            print(f"""{date[:10]} {description}
{of} -> {to}
{amount} {currency}""")
        else:
            print(f"""{date[:10]} {description}
{to}
{amount} {currency}""")


main()
