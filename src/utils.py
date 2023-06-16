import json
import operator


def open_file():
    """
    Функция загружает все данные и сохраняет их в переменную data из файла operations.json
    :return: Возвращает все операции клиента
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_executed():
    """
    Получает загруженные данные из open_file() и убирает отклоненные операции по ключу state
    :return: Возвращает отсортированные операции по дате от ближайшей к самой ранней
    """
    executed = open_file()
    state = []
    for i in executed:
        if i.get("state") == "EXECUTED":
            state.append(i)
    return sorted(state, key=operator.itemgetter("date"))


def output():
    """
    Получает из get_executed() отсортированные операции и получает последние 5 операций
    :return: Возвращает те самые 5 последних операций
    """
    count = 0
    item = 0
    executed = get_executed()
    state = []
    for _ in executed:
        count += 1
        item -= 1
        state.append(executed[item])
        if count == 5:
            break
    return state
