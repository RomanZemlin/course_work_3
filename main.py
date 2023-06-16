from functions import output

data = output()
for i in data:
    if i.get('from') == str:
        print(i.get('date'), i.get('description'), i.get('from'), i.get('to'), i.get('operationAmount'))
    else:
        print(i.get('date'), i.get('description'), i.get('to'), i.get('operationAmount'))