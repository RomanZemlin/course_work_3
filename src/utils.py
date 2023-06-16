import json
import operator


def open_file():
    with open('operations.json', "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_executed():
    executed = open_file()
    state = []
    for i in executed:
        if i.get("state") == "EXECUTED":
            state.append(i)
    return sorted(state, key=operator.itemgetter("date"))


def output():
    count = 0
    id = 0
    executed = get_executed()
    state = []
    for i in executed:
        count += 1
        id -= 1
        state.append(executed[id])
        if count == 5:
            break
    return state
